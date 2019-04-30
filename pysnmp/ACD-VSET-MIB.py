#
# PySNMP MIB module ACD-VSET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACD-VSET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:57:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, MibIdentifier, Integer32, ModuleIdentity, Unsigned32, ObjectIdentity, Bits, TimeTicks, Counter32, IpAddress, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "MibIdentifier", "Integer32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Bits", "TimeTicks", "Counter32", "IpAddress", "NotificationType", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
acdVSet = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 13))
acdVSet.setRevisions(('2012-01-11 01:00',))
if mibBuilder.loadTexts: acdVSet.setLastUpdated('201201110100Z')
if mibBuilder.loadTexts: acdVSet.setOrganization('Accedian Networks, Inc.')
acdVSetNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 0))
acdVSetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1))
acdVSetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2))
acdVSetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1))
class AcdVsetVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cvlan", 1), ("svlan", 2))

acdVSetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1), )
if mibBuilder.loadTexts: acdVSetConfigTable.setStatus('current')
acdVSetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1), ).setIndexNames((0, "ACD-VSET-MIB", "acdVSetConfigPolicyListID"), (0, "ACD-VSET-MIB", "acdVSetConfigID"))
if mibBuilder.loadTexts: acdVSetConfigEntry.setStatus('current')
acdVSetConfigPolicyListID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdVSetConfigPolicyListID.setStatus('current')
acdVSetConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: acdVSetConfigID.setStatus('current')
acdVSetConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigRowStatus.setStatus('current')
acdVSetConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigName.setStatus('current')
acdVSetConfigVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 5), AcdVsetVlanType().clone('cvlan')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanType.setStatus('current')
acdVSetConfigVlanIDs0to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanIDs0to1023.setStatus('current')
acdVSetConfigVlanIDs1024to2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanIDs1024to2047.setStatus('current')
acdVSetConfigVlanIDs2048to3071 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanIDs2048to3071.setStatus('current')
acdVSetConfigVlanIDs3072to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanIDs3072to4095.setStatus('current')
acdVSetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 1))
acdVSetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 2))
acdVSetConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 2, 1)).setObjects(("ACD-VSET-MIB", "acdVSetConfigRowStatus"), ("ACD-VSET-MIB", "acdVSetConfigName"), ("ACD-VSET-MIB", "acdVSetConfigVlanType"), ("ACD-VSET-MIB", "acdVSetConfigVlanIDs0to1023"), ("ACD-VSET-MIB", "acdVSetConfigVlanIDs1024to2047"), ("ACD-VSET-MIB", "acdVSetConfigVlanIDs2048to3071"), ("ACD-VSET-MIB", "acdVSetConfigVlanIDs3072to4095"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdVSetConfigGroup = acdVSetConfigGroup.setStatus('current')
acdVSetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 1, 1)).setObjects(("ACD-VSET-MIB", "acdVSetConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdVSetCompliance = acdVSetCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-VSET-MIB", acdVSetConformance=acdVSetConformance, acdVSetConfigGroup=acdVSetConfigGroup, acdVSetCompliance=acdVSetCompliance, acdVSetConfigID=acdVSetConfigID, PYSNMP_MODULE_ID=acdVSet, AcdVsetVlanType=AcdVsetVlanType, acdVSetConfigPolicyListID=acdVSetConfigPolicyListID, acdVSetConfig=acdVSetConfig, acdVSetConfigName=acdVSetConfigName, acdVSet=acdVSet, acdVSetConfigTable=acdVSetConfigTable, acdVSetConfigRowStatus=acdVSetConfigRowStatus, acdVSetConfigEntry=acdVSetConfigEntry, acdVSetConfigVlanIDs1024to2047=acdVSetConfigVlanIDs1024to2047, acdVSetCompliances=acdVSetCompliances, acdVSetGroups=acdVSetGroups, acdVSetNotifications=acdVSetNotifications, acdVSetConfigVlanType=acdVSetConfigVlanType, acdVSetConfigVlanIDs3072to4095=acdVSetConfigVlanIDs3072to4095, acdVSetMIBObjects=acdVSetMIBObjects, acdVSetConfigVlanIDs2048to3071=acdVSetConfigVlanIDs2048to3071, acdVSetConfigVlanIDs0to1023=acdVSetConfigVlanIDs0to1023)
