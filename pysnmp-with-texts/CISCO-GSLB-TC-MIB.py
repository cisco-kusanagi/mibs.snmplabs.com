#
# PySNMP MIB module CISCO-GSLB-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GSLB-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:59:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Bits, ModuleIdentity, ObjectIdentity, Counter32, Counter64, TimeTicks, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 583))
ciscoGslbTcMIB.setRevisions(('2007-02-23 00:00', '2006-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbTcMIB.setRevisionsDescriptions(("Added enumeration 'scriptedKal' to CiscoGslbKeepaliveMethod. Added enumeration 'init' to CiscoGslbAnswerStatus.", 'Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoGslbTcMIB.setLastUpdated('200702230000Z')
if mibBuilder.loadTexts: ciscoGslbTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbTcMIB.setDescription("This MIB module defines Textual Conventions and OBJECT-IDENTITIES for use in documents defining management information base (MIBs) modules for managing CISCO-GSLB-SYSTEM-MIB, CISCO-GSLB-DNS-MIB and CISCO-GSLB-HEALTH-MON-MIB (These MIB modules are used for a Global Server Load Balancing device(GSLB)). Acronyms and their description: CRA : Content Routing Agent - software that provides information to a GSLB device for content routing decisions and handles content routing requests from the GSLB device. D-Proxy : It is a local name server of the client which has initiated a DNS query for a domain. VIP : Virtual IP Addresses - they are used by server load balancing devices to represent content hosted on one or more servers under their control. The use of VIPs is to route content to the proper requesting host without exposing the device's internal IP address. Keepalive : A keepalive is an interaction between GSLB device and another device using a commonly supported protocol. It is used to periodically check if a resource is still active. DNS race : It is a method of resolving the proximity of the CRAs from the D-Proxy. In this method the GSLB device sends a request to all the CRAs directing them to respond to the D-Proxy at at the same time. The first response received by the D-proxy is, by default, considered to be the most proximate.")
class CiscoGslbNodeServices(TextualConvention, Integer32):
    description = "Defines the role of the GSLB device in a GSLB peer network: 'primary' : Provides GSLB services and active for peer configuration and management. 'standby' : Provides GSLB services and standby for peer configuration and management. 'secondary' : Provides GSLB services only, not peer configuration and management."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("primary", 1), ("standby", 2), ("secondary", 3))

class CiscoGslbPeerStatus(TextualConvention, Integer32):
    description = "Defines the status of a peer as known to this GSLB device. 'inactive' : GSLB peer device is waiting to be activated by the primary GSLB device it is registered with. 'offline' : GSLB device which is out-of-service. 'online' : GSLB device which is in service."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inactive", 1), ("offline", 2), ("online", 3))

class CiscoGslbAnswerType(TextualConvention, Integer32):
    description = "Defines the answer type. When a GSLB device receives a request from a D-proxy, it will resolve the request by pointing the D-proxy to one of the answers. The answer can be one of the following type: 'other' : The value 'other' has been provided so that the MIB may still be valid while new protocols emerge and the MIB has not been updated to enumerate them. 'vip' : Virtual IP address associated with SLB device or any other geographically dispersed device in global network deployment. 'ns' : IP Address of the NS that can answer queries that the GSLB device cannot resolve. 'cra' : CRAs that use a resolution process called DNS race to send identical and simultaneous responses back to a user's D-proxy."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("vip", 2), ("ns", 3), ("cra", 4))

class CiscoGslbKeepaliveTargetType(TextualConvention, Integer32):
    description = "Defines the answer type to which the keepalive is associated. The only exception being shared, where the keepalive can be associated with multiple answers, hence the name shared. 'other' : The value 'other' has been provided so that the MIB may still be valid while new protocols emerge and the MIB has not been updated to enumerate them. 'vip' : Keepalives associated with VIP answer. 'ns' : Keepalives associated with NS answer. 'cra' : Keepalives associated with CRA answer. 'shared' : Keepalives that may be shared among multiple VIP answers."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("vip", 2), ("ns", 3), ("cra", 4), ("shared", 5))

class CiscoGslbKeepaliveMethod(TextualConvention, Integer32):
    description = "Defines the keepalive method. A keepalive is an interaction between GSLB device and another device using a commonly supported protocol. This defines the protocol to be used by the keepalive when monitoring an answer. For example a keepalive for a VIP answer can have icmp/tcp/httphead/kalap method to monitor the health of answer. (Note: The keepaliveTargetType is VIP, since the answer is associated with a VIP type answer.) 'other' : The value 'other' has been provided so that the MIB may still be valid while new protocols emerge and the MIB has not been updated to enumerate them. 'none' : This is to prevent the GSLB device from taking the online status and load into account. Thus, the resource is always assumed to be online. 'icmp' : Internet Control Message Protocol(ICMP) packets are sent to the VIP address (or a shared keepalive address) for an answer to determine the Online status indicating connectivity to network. 'tcp' : To determine the Online status a TCP connection to remote device is established by performing three-way handshake sequence. The connection is then terminated. 'httphead' : A HTTP HEAD connection is established, the online status of the resource is returned in form of an HTTP Response, then the connection is terminated. 'kalap' : A detailed query is sent to primary and an optional secondary address to determine the online status and load of each specified address. 'ns' : A query is sent to the NS address to determine its online status by means of its ability to respond the query for the domain. 'cra' : It is used when testing CRA answer that respond to DNS race requests as it keeps track to the time required for a packet to reach the CRA and return to the GSLB device. 'scriptedKal' : It uses SNMP get request to fetch the load information from the target device. It enables the GSLB device to use third party application for fetching the load information from target."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("other", 1), ("none", 2), ("icmp", 3), ("tcp", 4), ("httphead", 5), ("kalap", 6), ("ns", 7), ("cra", 8), ("scriptedKal", 9))

class CiscoGslbKeepaliveConfigState(TextualConvention, Integer32):
    description = "Administrative configuration state for the keepalive. The keepalive can be activated/suspended by the administrator. This is used to define the present state of the keepalive. 'active' : The keepalive is administratively enabled. 'suspend' : The keepalive is administratively disabled."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("suspend", 2))

class CiscoGslbKeepaliveRate(TextualConvention, Integer32):
    description = "The rate associated with each keepalive method. It defines the rate at which the probing happens in-other-words how frequently the probing should happen. 'other' : The value 'other' has been provided so that the MIB may still be valid while new rates emerge and the MIB has not been updated to enumerate them. 'standard' : Uses the standard detection time. Each keepalive method has a standard detection time associated with it. 'fast' : Uses the user-selectable Number of Retries parameter to control the transmission rate. Number of retries is a user configurable parameter, which says the number times the target device has to be probed before declaring it offline."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("standard", 2), ("fast", 3))

class CiscoGslbTerminationMethod(TextualConvention, Integer32):
    description = "Some keepalives establish a connection and then terminate the connection as part of the process to determine the online status of the resource. For example, in a keepalive of method 'tcp', a connection is established to the target device while probing. GSS can terminate this connection in either of the following ways: 'other' : The value 'other' has been provided so that the MIB may still be valid while new methods emerge and the MIB has not been updated to enumerate them. 'reset' : Immediately terminates the connection by using a hard reset. 'graceful' : Initiates the graceful closing of the connection by using the standard three-way connection termination method."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("reset", 2), ("graceful", 3))

class CiscoGslbKeepaliveStatus(TextualConvention, Integer32):
    description = "Most recently known status of the keepalive. 'other' : The value 'other' has been provided so that the MIB may still be valid while new states emerge and the MIB has not been updated to enumerate them. 'offline' : The resource whose status is being determined by the keepalive is not available. 'online' : The resource is available and is in service. 'suspended' : The keepalive is suspended. 'init' : The keepalive is being initialized."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("offline", 2), ("online", 3), ("suspended", 4), ("init", 5))

class CiscoGslbAnswerStatus(TextualConvention, Integer32):
    description = "Most recently known status of the answer 'other' : The value 'other' has been provided so that the MIB may still be valid while new states emerge and the MIB has not been updated to enumerate them. 'offline' : The answer is not available as is determined by using the keepalives associated with the answer. 'online' : The answer is available and is in service. 'suspended' : The answer has been administratively disabled. 'init' : The answer is being initialized."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("offline", 2), ("online", 3), ("suspended", 4), ("init", 5))

class CiscoGslbAnswerAdminState(TextualConvention, Integer32):
    description = "Administrative configuration state for an answer. An answer can be activated/suspended by the administrator. This is used to define the present state of the answer. 'active' : The answer has been administratively enabled. 'suspended' : The answer has been administratively disabled."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("suspended", 1), ("active", 2))

class CiscoGslbKalapType(TextualConvention, Integer32):
    description = "Kalap is keepalive protocol, which sends a detailed query to primary and an optional secondary address to determine the online status and load of each specified address. Following are the different types in kalap method of keepalive: 'other' : The value 'other' has been provided so that the MIB may still be valid while new states emerge and the MIB has not been updated to enumerate them. 'kalapByVip' : In this type, only the VIP address is specified in the kalap request. The kalap queries the VIP to determine the online status. 'kalapByTag' : In this type, an alphanumeric tag associated with the VIP is specified in the kalap request. The kalap queries the VIP to determine the online status."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("kalapByVip", 2), ("kalapByTag", 3))

class CiscoGslbBalanceMethod(TextualConvention, Integer32):
    description = "A balance method is an algorithm for selecting the best server. Following are the different types of balance methods: 'other' : The value 'other' has been provided so that the MIB may still be valid while new states emerge and the MIB has not been updated to enumerate them. 'orderedList' : In this type, each resource within an answer group (for example, an SLB VIP or a name server) is assigned a number that corresponds to the rank of that answer within the group. The number assigned represents the order of the answer on the list. Subsequent VIPs or name servers on the list will only be used if preceding VIPs or name servers on the list are unavailable. 'roundRobin' : In this type, each resource within an answer group is tried in turn. The GSLB device cycles through the list of answers, selecting the next answer in line for each request. In this way, the device can resolve requests by evenly distributing the load among possible answers. 'weightedRR' : In this type, as performed by the round-robin balance method, the weighted round-robin method also cycles through a list of defined answers to choose each available answer in turn. However, with weighted round-robin, an additional weight factor is assigned to each answer, biasing the GSLB device towards certain servers so that they are used more often. 'leastLoaded' : In this type, the GSLB device resolves requests to the least loaded of all resources. 'hashed' : In this type, elements of the client's DNS proxy IP address and the requesting client's domain are extracted to create a unique value, referred to as a hash value. The unique hash value is attached to and used to identify a VIP that is chosen to serve the DNS query. 'boomerang' : This method is based on the concept that instantaneous proximity can be determined if a CRA within each data center sends an A-record (IP address) at the exact same time to the client's D-proxy. The DNS race method of DNS resolution gives all CRAs (Cisco content engines or content services switches) a chance at resolving a client request and allows for proximity to be determined without probing the client's D-proxy. The first A-record received by the D-proxy is, by default, considered to be the most proximate."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("orderedList", 2), ("roundRobin", 3), ("weightedRR", 4), ("leastLoaded", 5), ("hashed", 6), ("boomerang", 7))

mibBuilder.exportSymbols("CISCO-GSLB-TC-MIB", CiscoGslbNodeServices=CiscoGslbNodeServices, CiscoGslbAnswerAdminState=CiscoGslbAnswerAdminState, CiscoGslbKeepaliveMethod=CiscoGslbKeepaliveMethod, CiscoGslbKeepaliveRate=CiscoGslbKeepaliveRate, CiscoGslbKeepaliveTargetType=CiscoGslbKeepaliveTargetType, PYSNMP_MODULE_ID=ciscoGslbTcMIB, CiscoGslbAnswerStatus=CiscoGslbAnswerStatus, ciscoGslbTcMIB=ciscoGslbTcMIB, CiscoGslbPeerStatus=CiscoGslbPeerStatus, CiscoGslbKalapType=CiscoGslbKalapType, CiscoGslbTerminationMethod=CiscoGslbTerminationMethod, CiscoGslbAnswerType=CiscoGslbAnswerType, CiscoGslbKeepaliveConfigState=CiscoGslbKeepaliveConfigState, CiscoGslbKeepaliveStatus=CiscoGslbKeepaliveStatus, CiscoGslbBalanceMethod=CiscoGslbBalanceMethod)
