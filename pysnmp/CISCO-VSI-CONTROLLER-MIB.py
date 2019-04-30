#
# PySNMP MIB module CISCO-VSI-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VSI-CONTROLLER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, NotificationType, Gauge32, Bits, Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Counter64, iso, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Gauge32", "Bits", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Counter64", "iso", "Integer32", "TimeTicks")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoVSIControllerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 141))
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setLastUpdated('9906080000Z')
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setOrganization('Cisco Systems, Inc.')
class CvcControllerShelfLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("internal", 1), ("external", 2))

class CvcControllerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("par", 1), ("pnni", 2), ("lsc", 3))

cvcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 1))
cvcConfController = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1))
cvcConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1), )
if mibBuilder.loadTexts: cvcConfTable.setStatus('current')
cvcConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerID"))
if mibBuilder.loadTexts: cvcConfEntry.setStatus('current')
cvcConfControllerID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvcConfControllerID.setStatus('current')
cvcConfControllerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 2), CvcControllerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerType.setStatus('current')
cvcConfControllerShelfLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 3), CvcControllerShelfLocation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerShelfLocation.setStatus('current')
cvcConfControllerLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerLocation.setStatus('current')
cvcConfControllerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerName.setStatus('current')
cvcConfVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfVpi.setStatus('current')
cvcConfVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfVci.setStatus('current')
cvcConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfRowStatus.setStatus('current')
cvcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3))
cvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1))
cvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2))
cvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1, 1)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfGroup"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfGroupExternal"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcMIBCompliance = cvcMIBCompliance.setStatus('current')
cvcConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 1)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerType"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerShelfLocation"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerLocation"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerName"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcConfGroup = cvcConfGroup.setStatus('current')
cvcConfGroupExternal = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 2)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfVpi"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfVci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcConfGroupExternal = cvcConfGroupExternal.setStatus('current')
mibBuilder.exportSymbols("CISCO-VSI-CONTROLLER-MIB", cvcConfTable=cvcConfTable, cvcMIBGroups=cvcMIBGroups, cvcConfControllerType=cvcConfControllerType, cvcConfVpi=cvcConfVpi, CvcControllerShelfLocation=CvcControllerShelfLocation, cvcConfControllerLocation=cvcConfControllerLocation, cvcConfController=cvcConfController, cvcConfControllerName=cvcConfControllerName, PYSNMP_MODULE_ID=ciscoVSIControllerMIB, cvcConfControllerID=cvcConfControllerID, cvcConfGroupExternal=cvcConfGroupExternal, cvcMIBCompliance=cvcMIBCompliance, cvcConfEntry=cvcConfEntry, ciscoVSIControllerMIB=ciscoVSIControllerMIB, cvcConfControllerShelfLocation=cvcConfControllerShelfLocation, cvcConfRowStatus=cvcConfRowStatus, cvcConfGroup=cvcConfGroup, CvcControllerType=CvcControllerType, cvcConfVci=cvcConfVci, cvcMIBObjects=cvcMIBObjects, cvcMIBCompliances=cvcMIBCompliances, cvcMIBConformance=cvcMIBConformance)
