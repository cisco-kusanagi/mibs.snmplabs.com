#
# PySNMP MIB module ENTERASYS-ACTIVATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-ACTIVATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, Unsigned32, ModuleIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Counter32, IpAddress, Gauge32, MibIdentifier, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "ModuleIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Counter32", "IpAddress", "Gauge32", "MibIdentifier", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
etsysActivationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999))
etsysActivationMIB.setRevisions(('2002-04-18 14:54',))
if mibBuilder.loadTexts: etsysActivationMIB.setLastUpdated('200204181454Z')
if mibBuilder.loadTexts: etsysActivationMIB.setOrganization('Enterasys Networks, Inc')
etsysActivationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1))
class EnterasysKeyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noKey", 1), ("unknownKeyType", 2), ("productKey", 3), ("demoKey", 4))

class EnterasysFeature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("dot1xAuthentication", 1), ("pointToMultipoint", 2))

etsysActivationBaseBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1))
etsysMaxActivationKeyRow = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMaxActivationKeyRow.setStatus('current')
etsysActivationKeyTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2), )
if mibBuilder.loadTexts: etsysActivationKeyTable.setStatus('current')
etsysActivationKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1), ).setIndexNames((0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRow"))
if mibBuilder.loadTexts: etsysActivationKeyEntry.setStatus('current')
etsysActivationKeyRow = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: etsysActivationKeyRow.setStatus('current')
etsysActivationLicenseString = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationLicenseString.setStatus('current')
etsysActivationKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationKeyValue.setStatus('current')
etsysActivationKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 4), EnterasysKeyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysActivationKeyType.setStatus('current')
etsysActivationKeyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationKeyStatus.setStatus('current')
etsysActivationKeyFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3), )
if mibBuilder.loadTexts: etsysActivationKeyFeatureTable.setStatus('current')
etsysActivationKeyFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1), ).setIndexNames((0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRow"), (0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyFeature"))
if mibBuilder.loadTexts: etsysActivationKeyFeatureEntry.setStatus('current')
etsysActivationKeyFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1, 1), EnterasysFeature())
if mibBuilder.loadTexts: etsysActivationKeyFeature.setStatus('current')
etsysActivationKeyRestrictions = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysActivationKeyRestrictions.setStatus('current')
etsysActivationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2))
etsysActivationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 1))
etsysActivationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 2))
etsysActivationBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 1, 1)).setObjects(("ENTERASYS-ACTIVATION-MIB", "etsysMaxActivationKeyRow"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationLicenseString"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyValue"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyType"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyStatus"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRestrictions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysActivationBaseGroup = etsysActivationBaseGroup.setStatus('current')
etsysActivationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 2, 1)).setObjects(("ENTERASYS-ACTIVATION-MIB", "etsysActivationBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysActivationCompliance = etsysActivationCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-ACTIVATION-MIB", etsysActivationBaseBranch=etsysActivationBaseBranch, etsysActivationKeyTable=etsysActivationKeyTable, etsysActivationKeyFeatureTable=etsysActivationKeyFeatureTable, etsysActivationKeyRestrictions=etsysActivationKeyRestrictions, etsysActivationLicenseString=etsysActivationLicenseString, etsysActivationCompliances=etsysActivationCompliances, etsysActivationKeyFeature=etsysActivationKeyFeature, etsysActivationKeyEntry=etsysActivationKeyEntry, etsysActivationBaseGroup=etsysActivationBaseGroup, etsysActivationObjects=etsysActivationObjects, etsysActivationKeyFeatureEntry=etsysActivationKeyFeatureEntry, etsysActivationKeyStatus=etsysActivationKeyStatus, etsysActivationConformance=etsysActivationConformance, etsysActivationKeyType=etsysActivationKeyType, etsysActivationMIB=etsysActivationMIB, EnterasysKeyType=EnterasysKeyType, etsysActivationKeyValue=etsysActivationKeyValue, etsysActivationCompliance=etsysActivationCompliance, PYSNMP_MODULE_ID=etsysActivationMIB, EnterasysFeature=EnterasysFeature, etsysActivationGroups=etsysActivationGroups, etsysActivationKeyRow=etsysActivationKeyRow, etsysMaxActivationKeyRow=etsysMaxActivationKeyRow)
