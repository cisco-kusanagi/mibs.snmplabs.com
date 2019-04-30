#
# PySNMP MIB module MPLS-LDP-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-LDP-GENERIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:04:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpEntityObjects = mibBuilder.importSymbols("MPLS-LDP-MIB", "mplsLdpEntityLdpId", "mplsLdpEntityIndex", "mplsLdpEntityObjects")
mplsMIB, = mibBuilder.importSymbols("MPLS-TC-MIB", "mplsMIB")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, iso, ModuleIdentity, NotificationType, IpAddress, TimeTicks, Integer32, Unsigned32, Gauge32, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "ModuleIdentity", "NotificationType", "IpAddress", "TimeTicks", "Integer32", "Unsigned32", "Gauge32", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier")
RowStatus, DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "StorageType", "TextualConvention")
mplsLdpGenericMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 9999, 6))
mplsLdpGenericMIB.setRevisions(('2002-08-08 12:00',))
if mibBuilder.loadTexts: mplsLdpGenericMIB.setLastUpdated('200208081200Z')
if mibBuilder.loadTexts: mplsLdpGenericMIB.setOrganization('Multiprotocol Label Switching (mpls) Working Group')
mplsLdpGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9999, 6, 1))
mplsLdpGenericConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9999, 6, 3))
mplsLdpEntityGenericObjects = MibIdentifier((1, 3, 6, 1, 3, 97, 1, 2, 5))
mplsLdpEntityGenLRTable = MibTable((1, 3, 6, 1, 3, 97, 1, 2, 5, 1), )
if mibBuilder.loadTexts: mplsLdpEntityGenLRTable.setStatus('current')
mplsLdpEntityGenLREntry = MibTableRow((1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1), ).setIndexNames((0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenLRMin"), (0, "MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenLRMax"))
if mibBuilder.loadTexts: mplsLdpEntityGenLREntry.setStatus('current')
mplsLdpEntityGenLRMin = MibTableColumn((1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575)))
if mibBuilder.loadTexts: mplsLdpEntityGenLRMin.setStatus('current')
mplsLdpEntityGenLRMax = MibTableColumn((1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575)))
if mibBuilder.loadTexts: mplsLdpEntityGenLRMax.setStatus('current')
mplsLdpEntityGenIfIndexOrZero = MibTableColumn((1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenIfIndexOrZero.setStatus('current')
mplsLdpEntityGenLRStorageType = MibTableColumn((1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenLRStorageType.setStatus('current')
mplsLdpEntityGenLRRowStatus = MibTableColumn((1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenLRRowStatus.setStatus('current')
mplsLdpGenericGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 1))
mplsLdpGenericCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 2))
mplsLdpGenModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 2, 1)).setObjects(("MPLS-LDP-GENERIC-MIB", "mplsLdpGenericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenModuleFullCompliance = mplsLdpGenModuleFullCompliance.setStatus('current')
mplsLdpGenModuleROCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 2, 2)).setObjects(("MPLS-LDP-GENERIC-MIB", "mplsLdpGenericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenModuleROCompliance = mplsLdpGenModuleROCompliance.setStatus('current')
mplsLdpGenericGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 9999, 6, 3, 1, 1)).setObjects(("MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenIfIndexOrZero"), ("MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenLRStorageType"), ("MPLS-LDP-GENERIC-MIB", "mplsLdpEntityGenLRRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericGroup = mplsLdpGenericGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LDP-GENERIC-MIB", mplsLdpEntityGenericObjects=mplsLdpEntityGenericObjects, mplsLdpGenericConformance=mplsLdpGenericConformance, PYSNMP_MODULE_ID=mplsLdpGenericMIB, mplsLdpGenericObjects=mplsLdpGenericObjects, mplsLdpGenModuleROCompliance=mplsLdpGenModuleROCompliance, mplsLdpGenericCompliances=mplsLdpGenericCompliances, mplsLdpGenericGroup=mplsLdpGenericGroup, mplsLdpEntityGenLRMin=mplsLdpEntityGenLRMin, mplsLdpGenericMIB=mplsLdpGenericMIB, mplsLdpEntityGenLRTable=mplsLdpEntityGenLRTable, mplsLdpEntityGenLRStorageType=mplsLdpEntityGenLRStorageType, mplsLdpGenModuleFullCompliance=mplsLdpGenModuleFullCompliance, mplsLdpEntityGenLRRowStatus=mplsLdpEntityGenLRRowStatus, mplsLdpEntityGenLREntry=mplsLdpEntityGenLREntry, mplsLdpGenericGroups=mplsLdpGenericGroups, mplsLdpEntityGenLRMax=mplsLdpEntityGenLRMax, mplsLdpEntityGenIfIndexOrZero=mplsLdpEntityGenIfIndexOrZero)
