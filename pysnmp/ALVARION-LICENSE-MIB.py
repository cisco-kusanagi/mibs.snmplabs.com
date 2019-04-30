#
# PySNMP MIB module ALVARION-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-LICENSE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, MibIdentifier, NotificationType, Gauge32, iso, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibIdentifier", "NotificationType", "Gauge32", "iso", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29))
if mibBuilder.loadTexts: alvarionLicenseMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionLicenseMIB.setOrganization('Alvarion Ltd.')
alvarionLicenseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1))
coLicenseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1))
coLicenseFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1), )
if mibBuilder.loadTexts: coLicenseFeatureTable.setStatus('current')
coLicenseFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1), ).setIndexNames((0, "ALVARION-LICENSE-MIB", "coLicenseFeatureIndex"))
if mibBuilder.loadTexts: coLicenseFeatureEntry.setStatus('current')
coLicenseFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coLicenseFeatureIndex.setStatus('current')
coLicenseFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureName.setStatus('current')
coLicenseFeatureState = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureState.setStatus('current')
coLicenseFeatureEndingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureEndingDate.setStatus('current')
coLicenseFeatureRemainingDays = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureRemainingDays.setStatus('current')
alvarionLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2))
alvarionLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2, 1))
alvarionLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2, 2))
alvarionLicenseMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2, 1, 1)).setObjects(("ALVARION-LICENSE-MIB", "alvarionLicenseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionLicenseMIBCompliance = alvarionLicenseMIBCompliance.setStatus('current')
alvarionLicenseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2, 2, 1)).setObjects(("ALVARION-LICENSE-MIB", "coLicenseFeatureName"), ("ALVARION-LICENSE-MIB", "coLicenseFeatureState"), ("ALVARION-LICENSE-MIB", "coLicenseFeatureEndingDate"), ("ALVARION-LICENSE-MIB", "coLicenseFeatureRemainingDays"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionLicenseMIBGroup = alvarionLicenseMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-LICENSE-MIB", alvarionLicenseMIBCompliance=alvarionLicenseMIBCompliance, PYSNMP_MODULE_ID=alvarionLicenseMIB, alvarionLicenseMIBGroup=alvarionLicenseMIBGroup, coLicenseFeatureIndex=coLicenseFeatureIndex, coLicenseGroup=coLicenseGroup, alvarionLicenseMIBConformance=alvarionLicenseMIBConformance, alvarionLicenseMIB=alvarionLicenseMIB, alvarionLicenseMIBObjects=alvarionLicenseMIBObjects, coLicenseFeatureTable=coLicenseFeatureTable, coLicenseFeatureName=coLicenseFeatureName, coLicenseFeatureRemainingDays=coLicenseFeatureRemainingDays, coLicenseFeatureState=coLicenseFeatureState, alvarionLicenseMIBCompliances=alvarionLicenseMIBCompliances, alvarionLicenseMIBGroups=alvarionLicenseMIBGroups, coLicenseFeatureEntry=coLicenseFeatureEntry, coLicenseFeatureEndingDate=coLicenseFeatureEndingDate)
