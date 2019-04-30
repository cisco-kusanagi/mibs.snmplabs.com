#
# PySNMP MIB module XEDIA-L2DIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-L2DIAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ObjectIdentity, TimeTicks, IpAddress, Counter64, Integer32, Gauge32, iso, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "TimeTicks", "IpAddress", "Counter64", "Integer32", "Gauge32", "iso", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaL2DialMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 30))
if mibBuilder.loadTexts: xediaL2DialMIB.setLastUpdated('9902272155Z')
if mibBuilder.loadTexts: xediaL2DialMIB.setOrganization('Xedia Corp.')
l2DialObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 30, 1))
l2DialConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 30, 2))
l2DialStatusTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1), )
if mibBuilder.loadTexts: l2DialStatusTable.setStatus('current')
l2DialStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1), ).setIndexNames((0, "XEDIA-L2DIAL-MIB", "l2DialStatusIpAddress"))
if mibBuilder.loadTexts: l2DialStatusEntry.setStatus('current')
l2DialStatusIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: l2DialStatusIpAddress.setStatus('current')
l2DialStatusSublayer = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 30, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2DialStatusSublayer.setStatus('current')
l2DialCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 1))
l2DialGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 2))
l2DialCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 1, 1)).setObjects(("XEDIA-L2DIAL-MIB", "l2DialStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2DialCompliance = l2DialCompliance.setStatus('current')
l2DialStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 30, 2, 2, 1)).setObjects(("XEDIA-L2DIAL-MIB", "l2DialStatusSublayer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2DialStatusGroup = l2DialStatusGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-L2DIAL-MIB", l2DialGroups=l2DialGroups, l2DialStatusIpAddress=l2DialStatusIpAddress, l2DialObjects=l2DialObjects, PYSNMP_MODULE_ID=xediaL2DialMIB, xediaL2DialMIB=xediaL2DialMIB, l2DialConformance=l2DialConformance, l2DialStatusEntry=l2DialStatusEntry, l2DialStatusSublayer=l2DialStatusSublayer, l2DialStatusTable=l2DialStatusTable, l2DialCompliance=l2DialCompliance, l2DialCompliances=l2DialCompliances, l2DialStatusGroup=l2DialStatusGroup)
