#
# PySNMP MIB module SNMP-USM-HMAC-SHA2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-USM-HMAC-SHA2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
snmpAuthProtocols, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpAuthProtocols")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, mib_2, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, NotificationType, IpAddress, Counter32, Integer32, MibIdentifier, Counter64, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "mib-2", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "NotificationType", "IpAddress", "Counter32", "Integer32", "MibIdentifier", "Counter64", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpUsmHmacSha2MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 235))
snmpUsmHmacSha2MIB.setRevisions(('2016-04-18 00:00', '2015-10-14 00:00',))
if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setLastUpdated('201604180000Z')
if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setOrganization('SNMPv3 Working Group')
usmHMAC128SHA224AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 4))
if mibBuilder.loadTexts: usmHMAC128SHA224AuthProtocol.setStatus('current')
usmHMAC192SHA256AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 5))
if mibBuilder.loadTexts: usmHMAC192SHA256AuthProtocol.setStatus('current')
usmHMAC256SHA384AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 6))
if mibBuilder.loadTexts: usmHMAC256SHA384AuthProtocol.setStatus('current')
usmHMAC384SHA512AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 7))
if mibBuilder.loadTexts: usmHMAC384SHA512AuthProtocol.setStatus('current')
mibBuilder.exportSymbols("SNMP-USM-HMAC-SHA2-MIB", usmHMAC384SHA512AuthProtocol=usmHMAC384SHA512AuthProtocol, usmHMAC256SHA384AuthProtocol=usmHMAC256SHA384AuthProtocol, usmHMAC192SHA256AuthProtocol=usmHMAC192SHA256AuthProtocol, PYSNMP_MODULE_ID=snmpUsmHmacSha2MIB, usmHMAC128SHA224AuthProtocol=usmHMAC128SHA224AuthProtocol, snmpUsmHmacSha2MIB=snmpUsmHmacSha2MIB)
