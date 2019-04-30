#
# PySNMP MIB module TPLINK-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-LLDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, NotificationType, TimeTicks, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Gauge32, iso, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "NotificationType", "TimeTicks", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Gauge32", "iso", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 35))
tplinkLldpMIB.setRevisions(('2012-12-13 17:30',))
if mibBuilder.loadTexts: tplinkLldpMIB.setLastUpdated('201212131730Z')
if mibBuilder.loadTexts: tplinkLldpMIB.setOrganization('TPLINK')
tplinkLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1))
tplinkLldpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 2))
mibBuilder.exportSymbols("TPLINK-LLDP-MIB", PYSNMP_MODULE_ID=tplinkLldpMIB, tplinkLldpMIB=tplinkLldpMIB, tplinkLldpMIBObjects=tplinkLldpMIBObjects, tplinkLldpMIBNotifications=tplinkLldpMIBNotifications)
