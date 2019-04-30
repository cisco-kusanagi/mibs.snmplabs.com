#
# PySNMP MIB module HM2-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, TimeTicks, Gauge32, IpAddress, iso, Bits, ModuleIdentity, ObjectIdentity, Counter32, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "TimeTicks", "Gauge32", "IpAddress", "iso", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter32", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2QosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 32))
hm2QosMib.setRevisions(('2011-03-16 00:00',))
if mibBuilder.loadTexts: hm2QosMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2QosMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2QosMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 0))
hm2QosMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1))
hm2QosFirstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1, 1))
hm2QosNextGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1, 2))
mibBuilder.exportSymbols("HM2-QOS-MIB", hm2QosMibNotifications=hm2QosMibNotifications, PYSNMP_MODULE_ID=hm2QosMib, hm2QosNextGroup=hm2QosNextGroup, hm2QosFirstGroup=hm2QosFirstGroup, hm2QosMib=hm2QosMib, hm2QosMibObjects=hm2QosMibObjects)
