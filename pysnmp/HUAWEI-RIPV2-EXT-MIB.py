#
# PySNMP MIB module HUAWEI-RIPV2-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-RIPV2-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:36:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Gauge32, Unsigned32, Counter32, IpAddress, MibIdentifier, ModuleIdentity, TimeTicks, Counter64, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Gauge32", "Unsigned32", "Counter32", "IpAddress", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Counter64", "ObjectIdentity", "iso")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hwRipv2Ext = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120))
if mibBuilder.loadTexts: hwRipv2Ext.setLastUpdated('200605261430Z')
if mibBuilder.loadTexts: hwRipv2Ext.setOrganization('Huawei Technologies Co., Ltd.')
hwRip2ProcInstTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1), )
if mibBuilder.loadTexts: hwRip2ProcInstTable.setStatus('current')
hwRip2ProcInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1, 1), ).setIndexNames((0, "HUAWEI-RIPV2-EXT-MIB", "hwRip2ProcessId"))
if mibBuilder.loadTexts: hwRip2ProcInstEntry.setStatus('current')
hwRip2ProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hwRip2ProcessId.setStatus('current')
hwRip2VrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRip2VrfName.setStatus('current')
hwRip2CurrentProcId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwRip2CurrentProcId.setStatus('current')
hwRip2Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2))
hwRip2Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2, 1))
hwRip2Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2, 2))
hwRip2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2, 2, 1)).setObjects(("HUAWEI-RIPV2-EXT-MIB", "hwRip2ExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRip2Compliance = hwRip2Compliance.setStatus('current')
hwRip2ExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2, 1, 2)).setObjects(("HUAWEI-RIPV2-EXT-MIB", "hwRip2VrfName"), ("HUAWEI-RIPV2-EXT-MIB", "hwRip2CurrentProcId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRip2ExtGroup = hwRip2ExtGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-RIPV2-EXT-MIB", hwRip2Groups=hwRip2Groups, PYSNMP_MODULE_ID=hwRipv2Ext, hwRipv2Ext=hwRipv2Ext, hwRip2Conformance=hwRip2Conformance, hwRip2ProcessId=hwRip2ProcessId, hwRip2CurrentProcId=hwRip2CurrentProcId, hwRip2ProcInstTable=hwRip2ProcInstTable, hwRip2Compliances=hwRip2Compliances, hwRip2Compliance=hwRip2Compliance, hwRip2ProcInstEntry=hwRip2ProcInstEntry, hwRip2ExtGroup=hwRip2ExtGroup, hwRip2VrfName=hwRip2VrfName)
