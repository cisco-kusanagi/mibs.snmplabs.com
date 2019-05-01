#
# PySNMP MIB module HPOV-SNMPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPOV-SNMPSEC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, MibIdentifier, Gauge32, iso, enterprises, Bits, Integer32, Unsigned32, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Gauge32", "iso", "enterprises", "Bits", "Integer32", "Unsigned32", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
openView = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17))
class OVTDAddress(TextualConvention, OctetString):
    reference = 'RFC 1906, Transport Mappings for SNMP Version 2'
    description = 'Denotes a transport domain and address, much like the TDomain and TAddress textual convention pair defined in RFC 1902, yet in a more compact representation. The first octet identifies the transport domain. This value directly corresponds to the value of the transport domain object sub-identifier, as defined in RFC1906, that is subordinate to iso.org.dod.internet.snmpV2.snmpDomains. The remaining octets conform to the transport address syntax associated with the specified transport domain. For example, a value of 1 in the first octet corresponds to snmpUDPDomain, so the remaining octets conform to the syntax of snmpUDPAddress. For convienence, the mappings are summarized as follows. Note that UDP/IP and IPX are fixed length; CLNS, CONS and DDP are variable length. OVTDAddress octets Domain 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15... ====== == == == == == == == == == == == == == == == UDP/IP 1 <ip-address> <port> CLNS 2 <n> <nsap-address..n> <t-selector...m> CONS 3 <n> <nsap-address..n> <t-selector...m> DDP 4 <n> <object...n><p><type..p><q><zone...q> IPX 5 <net-number> <physical-addres> <sock> '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

hpOVSNMPSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 5))
hpOVSecureTarget = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 5, 1), OVTDAddress())
if mibBuilder.loadTexts: hpOVSecureTarget.setStatus('current')
if mibBuilder.loadTexts: hpOVSecureTarget.setDescription('The transport domain/address of the intended destination or original source of an SNMP message forwarded through an OV/SNMPv2 Security Proxy. This object is not exposed to the OV application nor the target SNMP agent. It is used only within communication between the OpenView SNMP protocol engine and an SNMPv2 Security Proxy, as follows: o An instance of this object is appended to, and subsequently stripped from, all messages sent between the OV SNMP protocol engine and an SNMPv2 security proxy. o An instance of this object in messages sent from the OVSNMP protocol engine to the SNMPv2 security proxy identifies the intended destination of the SNMP message. o An instance of this object in messages received by the OVSNMP protocol engine from the SNMPv2 security proxy identifies the original source of the SNMP message.')
mibBuilder.exportSymbols("HPOV-SNMPSEC-MIB", hpOVSecureTarget=hpOVSecureTarget, nm=nm, hpOVSNMPSecurity=hpOVSNMPSecurity, hp=hp, OVTDAddress=OVTDAddress, openView=openView)
