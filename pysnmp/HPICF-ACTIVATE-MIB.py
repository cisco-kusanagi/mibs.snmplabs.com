#
# PySNMP MIB module HPICF-ACTIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPICF-ACTIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:24:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, TimeTicks, Integer32, Unsigned32, IpAddress, iso, Counter64, NotificationType, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Integer32", "Unsigned32", "IpAddress", "iso", "Counter64", "NotificationType", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hpicfActivateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129))
hpicfActivateMIB.setRevisions(('2016-05-03 00:00',))
if mibBuilder.loadTexts: hpicfActivateMIB.setLastUpdated('201605030000Z')
if mibBuilder.loadTexts: hpicfActivateMIB.setOrganization('HPE Networking')
hpicfActivateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1))
hpicfActivateConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2))
hpicfActivateSoftwareUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfActivateSoftwareUpdateMode.setStatus('current')
hpicfActivateProvisionMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfActivateProvisionMode.setStatus('current')
hpicfActivateMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1))
hpicfActivateMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2))
hpicfActivateMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1, 1)).setObjects(("HPICF-ACTIVATE-MIB", "hpicfActivateConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfActivateMIBCompliance = hpicfActivateMIBCompliance.setStatus('current')
hpicfActivateConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2, 1)).setObjects(("HPICF-ACTIVATE-MIB", "hpicfActivateSoftwareUpdateMode"), ("HPICF-ACTIVATE-MIB", "hpicfActivateProvisionMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfActivateConfigGroup = hpicfActivateConfigGroup.setStatus('current')
mibBuilder.exportSymbols("HPICF-ACTIVATE-MIB", hpicfActivateConformance=hpicfActivateConformance, PYSNMP_MODULE_ID=hpicfActivateMIB, hpicfActivateMIB=hpicfActivateMIB, hpicfActivateConfigGroup=hpicfActivateConfigGroup, hpicfActivateSoftwareUpdateMode=hpicfActivateSoftwareUpdateMode, hpicfActivateMIBGroups=hpicfActivateMIBGroups, hpicfActivateMIBCompliances=hpicfActivateMIBCompliances, hpicfActivateMIBCompliance=hpicfActivateMIBCompliance, hpicfActivateProvisionMode=hpicfActivateProvisionMode, hpicfActivateObjects=hpicfActivateObjects)
