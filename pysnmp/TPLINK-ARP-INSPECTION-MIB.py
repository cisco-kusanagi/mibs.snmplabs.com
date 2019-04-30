#
# PySNMP MIB module TPLINK-ARP-INSPECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ARP-INSPECTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, ObjectIdentity, MibIdentifier, IpAddress, ModuleIdentity, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ObjectIdentity", "MibIdentifier", "IpAddress", "ModuleIdentity", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkArpInspectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 28))
tplinkArpInspectionMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkArpInspectionMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkArpInspectionMIB.setOrganization('TPLINK')
tplinkArpInspectionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1))
tplinkArpInspectionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 28, 2))
mibBuilder.exportSymbols("TPLINK-ARP-INSPECTION-MIB", tplinkArpInspectionNotifications=tplinkArpInspectionNotifications, tplinkArpInspectionMIB=tplinkArpInspectionMIB, PYSNMP_MODULE_ID=tplinkArpInspectionMIB, tplinkArpInspectionMIBObjects=tplinkArpInspectionMIBObjects)
