#
# PySNMP MIB module ATDHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATDHCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
atiProduct, atswitchMib, mibObject, alliedTelesyn = mibBuilder.importSymbols("ATSWTCH2-MIB", "atiProduct", "atswitchMib", "mibObject", "alliedTelesyn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, Integer32, iso, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ObjectIdentity, enterprises, NotificationType, TimeTicks, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Integer32", "iso", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ObjectIdentity", "enterprises", "NotificationType", "TimeTicks", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    pass

atswitchDHCPGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 10, 11))
atswitchDHCPSysGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1))
atswitchDHCPTimerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2))
atswitchDHCPCurrentDHCPClientAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPCurrentDHCPClientAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atswitchDHCPCurrentDHCPClientAddress.setDescription(' Current IP address of the client. To start with,it might be null . This is filled by the server when sending a DHCPOFFER and the client uses the most comfortable offer from offers sent by different DHCP servers. A DHCPREQUEST packet is sent with the Client address agreed upon to the selected server ( Broadcast). Server Acks back this packet which is where Client/Server moves to the Bound state. Once reached into Bound state, the client address is made the official address on the client. ')
atswitchDHCPSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: atswitchDHCPSubnetMask.setDescription(' When the client/server reaches the BOUND state, this is one of the parameters set by the server. ')
atswitchDHCPCurrentRelayAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPCurrentRelayAgentAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atswitchDHCPCurrentRelayAgentAddress.setDescription(' The IP address of the DHCP relay Agent on the same subnet. Normally there will be no DHCP server on each of the subnet and this Relay Agent will act in sending server accross the subnets. There might not be any relay agent. This depends on the network Toplogy like where is the DHCP server and DHCP client. ')
atswitchDHCPNextDHCPServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPNextDHCPServerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atswitchDHCPNextDHCPServerAddress.setDescription(' The IP address of the next DHCP server to be used during bootstrap. This address is sent by the DHCP server in the messages DHCPOFFER, DHCPACK,DHCPNACK. ')
atswitchDHCPLeaseTimer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPLeaseTimer.setStatus('mandatory')
if mibBuilder.loadTexts: atswitchDHCPLeaseTimer.setDescription(' When the client/server reaches the BOUND state, this is one of the parameters set by the server. The lease time period in seconds for the DHCP client for using IP address on lease from the server. At the end of 50% of this timer a renewal request is sent by the client . This is the next Object atswitchDHCPRenewalTimer. ')
atswitchDHCPReacquisitionTimer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPReacquisitionTimer.setStatus('mandatory')
if mibBuilder.loadTexts: atswitchDHCPReacquisitionTimer.setDescription(" When the client/server reaches the BOUND state, this is one of the parameters set by the server. Mentioned in RFC2131 4.4.5 as T1, this renewal time period in secs for the DHCP client is for using IP address on lease from the server Once the Reacquisition Timer period in secs afetr the lease period is reached, the client sends a DHCPREQUEST to the DHCP server reque- -sting for renewal of the lease. Default would be 50% of the Lease timer which is represeneted by the above object. The client moves from BOUND to RENEW state once the DHCPREQUEST is sent after time T1 secs is passed from the start of to release time. T1 is always less than T2 ( see below for 'T2') which is lesss than the lease Timer period. ")
atswitchDHCPExpirationTimer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPExpirationTimer.setStatus('mandatory')
if mibBuilder.loadTexts: atswitchDHCPExpirationTimer.setDescription(' When the client/server reaches the BOUND state, this is one of the parameters set by the server. Mentioned in RFC2131 4.4.5 as T2,this Expiration time period in secs is the time period in secs during which DHCP has gone through the BOUND->RENEWAL state. After T1 secs and when the state machine reaches T2 secs, ( T1 < T2 < lease period), DHCP client sends another DHCPREQUEST to the server asking the server to renew the lease for the IP parameters. By default it would be 87.5% of the Lease timer .If there is DHCPACK then the DHCP client moves from REBIND to BOUND. Else it moves to INIT state where it starts all over again sending a request for DHCPDISCOVER. ')
mibBuilder.exportSymbols("ATDHCP-MIB", atswitchDHCPSubnetMask=atswitchDHCPSubnetMask, atswitchDHCPTimerGroup=atswitchDHCPTimerGroup, Timeout=Timeout, atswitchDHCPCurrentRelayAgentAddress=atswitchDHCPCurrentRelayAgentAddress, atswitchDHCPGroup=atswitchDHCPGroup, atswitchDHCPReacquisitionTimer=atswitchDHCPReacquisitionTimer, BridgeId=BridgeId, MacAddress=MacAddress, atswitchDHCPSysGroup=atswitchDHCPSysGroup, atswitchDHCPExpirationTimer=atswitchDHCPExpirationTimer, atswitchDHCPNextDHCPServerAddress=atswitchDHCPNextDHCPServerAddress, atswitchDHCPLeaseTimer=atswitchDHCPLeaseTimer, atswitchDHCPCurrentDHCPClientAddress=atswitchDHCPCurrentDHCPClientAddress)
