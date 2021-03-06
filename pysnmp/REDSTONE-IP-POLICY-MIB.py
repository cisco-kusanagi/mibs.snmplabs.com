#
# PySNMP MIB module REDSTONE-IP-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-IP-POLICY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, Gauge32, ObjectIdentity, iso, MibIdentifier, Bits, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity", "iso", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "IpAddress", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rsIpPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 13))
rsIpPolicyMIB.setRevisions(('1998-01-01 00:00',))
if mibBuilder.loadTexts: rsIpPolicyMIB.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: rsIpPolicyMIB.setOrganization('Redstone Communications, Inc.')
rsIpPolicyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1))
rsIpAccessList = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1))
rsIpAccessListTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1), )
if mibBuilder.loadTexts: rsIpAccessListTable.setStatus('current')
rsIpAccessListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1), ).setIndexNames((0, "REDSTONE-IP-POLICY-MIB", "rsIpAccessListId"), (0, "REDSTONE-IP-POLICY-MIB", "rsIpAccessListElemId"))
if mibBuilder.loadTexts: rsIpAccessListEntry.setStatus('current')
rsIpAccessListId = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 199)))
if mibBuilder.loadTexts: rsIpAccessListId.setStatus('current')
rsIpAccessListElemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)))
if mibBuilder.loadTexts: rsIpAccessListElemId.setStatus('current')
rsIpAccessListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListRowStatus.setStatus('current')
rsIpAccessListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("permit", 0), ("deny", 1))).clone('permit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListAction.setStatus('current')
rsIpAccessListSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 5), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListSrc.setStatus('current')
rsIpAccessListSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 6), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListSrcMask.setStatus('current')
rsIpAccessListDst = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 7), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListDst.setStatus('current')
rsIpAccessListDstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 8), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListDstMask.setStatus('current')
rsIpAccessListProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListProtocol.setStatus('current')
rsIpPolicyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4))
rsIpPolicyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 1))
rsIpPolicyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 2))
rsIpPolicyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 1, 1)).setObjects(("REDSTONE-IP-POLICY-MIB", "rsIpAccessListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIpPolicyCompliance = rsIpPolicyCompliance.setStatus('current')
rsIpAccessListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 2, 1)).setObjects(("REDSTONE-IP-POLICY-MIB", "rsIpAccessListRowStatus"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListAction"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListSrc"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListSrcMask"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListDst"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListDstMask"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIpAccessListGroup = rsIpAccessListGroup.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-IP-POLICY-MIB", rsIpAccessListSrc=rsIpAccessListSrc, rsIpPolicyConformance=rsIpPolicyConformance, rsIpAccessListEntry=rsIpAccessListEntry, rsIpPolicyObjects=rsIpPolicyObjects, rsIpAccessListGroup=rsIpAccessListGroup, rsIpAccessListId=rsIpAccessListId, rsIpAccessListElemId=rsIpAccessListElemId, rsIpAccessListSrcMask=rsIpAccessListSrcMask, PYSNMP_MODULE_ID=rsIpPolicyMIB, rsIpPolicyCompliances=rsIpPolicyCompliances, rsIpPolicyMIB=rsIpPolicyMIB, rsIpAccessListDstMask=rsIpAccessListDstMask, rsIpAccessList=rsIpAccessList, rsIpAccessListRowStatus=rsIpAccessListRowStatus, rsIpPolicyCompliance=rsIpPolicyCompliance, rsIpAccessListTable=rsIpAccessListTable, rsIpAccessListProtocol=rsIpAccessListProtocol, rsIpAccessListDst=rsIpAccessListDst, rsIpPolicyGroups=rsIpPolicyGroups, rsIpAccessListAction=rsIpAccessListAction)
