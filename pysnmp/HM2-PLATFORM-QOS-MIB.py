#
# PySNMP MIB module HM2-PLATFORM-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, IpAddress, Unsigned32, TimeTicks, Counter32, MibIdentifier, Bits, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "IpAddress", "Unsigned32", "TimeTicks", "Counter32", "MibIdentifier", "Bits", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2PlatformQoS = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 3))
hm2PlatformQoS.setRevisions(('2011-10-28 00:00',))
if mibBuilder.loadTexts: hm2PlatformQoS.setLastUpdated('201110280000Z')
if mibBuilder.loadTexts: hm2PlatformQoS.setOrganization('Hirschmann Automation and Control GmbH')
mibBuilder.exportSymbols("HM2-PLATFORM-QOS-MIB", hm2PlatformQoS=hm2PlatformQoS, PYSNMP_MODULE_ID=hm2PlatformQoS)
