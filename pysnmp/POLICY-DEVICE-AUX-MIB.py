#
# PySNMP MIB module POLICY-DEVICE-AUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POLICY-DEVICE-AUX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, NotificationType, ObjectIdentity, Counter64, experimental, Integer32, ModuleIdentity, IpAddress, TimeTicks, Gauge32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter64", "experimental", "Integer32", "ModuleIdentity", "IpAddress", "TimeTicks", "Gauge32", "Counter32", "Bits")
StorageType, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TextualConvention", "DisplayString", "RowStatus")
policyDeviceAuxMib = ModuleIdentity((1, 3, 6, 1, 3, 999))
if mibBuilder.loadTexts: policyDeviceAuxMib.setLastUpdated('200007121800Z')
if mibBuilder.loadTexts: policyDeviceAuxMib.setOrganization('IETF RAP WG')
policyDeviceAuxObjects = MibIdentifier((1, 3, 6, 1, 3, 999, 1))
policyDeviceAuxConformance = MibIdentifier((1, 3, 6, 1, 3, 999, 2))
policyDeviceConfig = MibIdentifier((1, 3, 6, 1, 3, 999, 1, 1))
class Role(TextualConvention, OctetString):
    reference = 'Policy Core Information Model, draft-ietf-policy-core-info-model-06.txt'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class RoleCombination(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

policyInterfaceTable = MibTable((1, 3, 6, 1, 3, 999, 1, 1, 1), )
if mibBuilder.loadTexts: policyInterfaceTable.setStatus('current')
policyInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 999, 1, 1, 1, 1), ).setIndexNames((0, "POLICY-DEVICE-AUX-MIB", "policyInterfaceIfIndex"))
if mibBuilder.loadTexts: policyInterfaceEntry.setStatus('current')
policyInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: policyInterfaceIfIndex.setStatus('current')
policyInterfaceRoleCombo = MibTableColumn((1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 2), RoleCombination()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyInterfaceRoleCombo.setStatus('current')
policyInterfaceStorage = MibTableColumn((1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyInterfaceStorage.setStatus('current')
policyInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyInterfaceStatus.setStatus('current')
policyDeviceCompliances = MibIdentifier((1, 3, 6, 1, 3, 999, 2, 1))
policyDeviceGroups = MibIdentifier((1, 3, 6, 1, 3, 999, 2, 2))
policyDeviceCompliance = ModuleCompliance((1, 3, 6, 1, 3, 999, 2, 1, 1)).setObjects(("POLICY-DEVICE-AUX-MIB", "policyInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyDeviceCompliance = policyDeviceCompliance.setStatus('current')
policyInterfaceGroup = ObjectGroup((1, 3, 6, 1, 3, 999, 2, 2, 1)).setObjects(("POLICY-DEVICE-AUX-MIB", "policyInterfaceRoleCombo"), ("POLICY-DEVICE-AUX-MIB", "policyInterfaceStorage"), ("POLICY-DEVICE-AUX-MIB", "policyInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyInterfaceGroup = policyInterfaceGroup.setStatus('current')
mibBuilder.exportSymbols("POLICY-DEVICE-AUX-MIB", policyInterfaceRoleCombo=policyInterfaceRoleCombo, policyDeviceAuxObjects=policyDeviceAuxObjects, policyDeviceConfig=policyDeviceConfig, policyInterfaceEntry=policyInterfaceEntry, policyInterfaceStatus=policyInterfaceStatus, policyDeviceCompliance=policyDeviceCompliance, policyInterfaceTable=policyInterfaceTable, Role=Role, policyInterfaceGroup=policyInterfaceGroup, policyDeviceCompliances=policyDeviceCompliances, RoleCombination=RoleCombination, PYSNMP_MODULE_ID=policyDeviceAuxMib, policyDeviceAuxMib=policyDeviceAuxMib, policyInterfaceStorage=policyInterfaceStorage, policyDeviceAuxConformance=policyDeviceAuxConformance, policyInterfaceIfIndex=policyInterfaceIfIndex, policyDeviceGroups=policyDeviceGroups)
