import streamlit as st
import dns.resolver

"""
# DNS Utility  🙀 :heart_eyes_cat:
"""

domain_name=st.text_input('Domain name', 'www.yahoo.com')
records=['A','AAAA','CNAME','MX','NS','SOA','TXT']

# Basic DNS query
for record in records:
    try:
        for rdata in dns.resolver.resolve(domain_name, record) :
            st.write(f"{record}:   {rdata}")
            break
    except dns.resolver.NoAnswer:
        st.write(f"{record}: The DNS response does not contain an answer to the question")
    except dns.resolver.NoMetaqueries:
        st.write(f"{record}: DNS metaqueries are not allowed.")
    except dns.resolver.NoNameservers:
        st.write(f"{record}: All nameservers failed to answer the query.")
    except dns.resolver.NoRootSOA:
        st.write(f"{record}: There is no SOA RR at the DNS root name. This should never happen!")
    except dns.resolver.NotAbsolute:
        st.write(f"{record}: An absolute domain name is required but a relative name was provided.")
    except dns.resolver.NXDOMAIN:
        st.write(f"{record}: The DNS query name does not exist.")
    except dns.resolver.YXDOMAIN:
        st.write(f"{record}: The DNS query name is too long after DNAME substitution.")
    except dns.resolver.Timeout:
        st.write(f"{record}: The DNS operation timed out.")
