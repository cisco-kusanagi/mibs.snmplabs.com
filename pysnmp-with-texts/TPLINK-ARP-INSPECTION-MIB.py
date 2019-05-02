#
# PySNMP MIB module TPLINK-ARP-INSPECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ARP-INSPECTION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, Counter64, ModuleIdentity, MibIdentifier, Integer32, ObjectIdentity, iso, NotificationType, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity", "MibIdentifier", "Integer32", "ObjectIdentity", "iso", "NotificationType", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkArpInspectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 28))
tplinkArpInspectionMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkArpInspectionMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkArpInspectionMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkArpInspectionMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkArpInspectionMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkArpInspectionMIB.setDescription('Private MIB for Arp Inspection configuration.')
tplinkArpInspectionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1))
tplinkArpInspectionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 28, 2))
mibBuilder.exportSymbols("TPLINK-ARP-INSPECTION-MIB", tplinkArpInspectionMIBObjects=tplinkArpInspectionMIBObjects, PYSNMP_MODULE_ID=tplinkArpInspectionMIB, tplinkArpInspectionMIB=tplinkArpInspectionMIB, tplinkArpInspectionNotifications=tplinkArpInspectionNotifications)
