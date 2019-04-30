#
# PySNMP MIB module ENTERASYS-8021X-REKEYING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-8021X-REKEYING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
dot1xPaePortNumber, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, TimeTicks, NotificationType, MibIdentifier, Unsigned32, Gauge32, Counter64, Counter32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "TimeTicks", "NotificationType", "MibIdentifier", "Unsigned32", "Gauge32", "Counter64", "Counter32", "IpAddress", "Integer32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
etsys8021xRekeyingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17))
etsys8021xRekeyingMIB.setRevisions(('2004-07-14 15:07', '2002-03-07 20:06',))
if mibBuilder.loadTexts: etsys8021xRekeyingMIB.setLastUpdated('200407141507Z')
if mibBuilder.loadTexts: etsys8021xRekeyingMIB.setOrganization('Enterasys Networks, Inc')
etsysDot1xRekeyingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1))
etsysDot1xRekeyBaseBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1))
etsysDot1xRekeyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1), )
if mibBuilder.loadTexts: etsysDot1xRekeyConfigTable.setStatus('current')
etsysDot1xRekeyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: etsysDot1xRekeyConfigEntry.setStatus('current')
etsysDot1xRekeyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyEnabled.setStatus('current')
etsysDot1xRekeyPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 2), Unsigned32().clone(1800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyPeriod.setStatus('current')
etsysDot1xRekeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("keylen40", 1), ("keylen128", 2))).clone('keylen128')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyLength.setStatus('current')
etsysDot1xRekeyAsymmetric = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyAsymmetric.setStatus('current')
etsysDot1xRekeyPairwise = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyPairwise.setStatus('current')
etsysDot1xRekeyingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2))
etsysDot1xRekeyingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1))
etsysDot1xRekeyingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 2))
etsysDot1xRekeyingBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1, 1)).setObjects(("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyPeriod"), ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyEnabled"), ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyLength"), ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyAsymmetric"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1xRekeyingBaseGroup = etsysDot1xRekeyingBaseGroup.setStatus('current')
etsysDot1xRekeyingPairwiseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1, 2)).setObjects(("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyPairwise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1xRekeyingPairwiseGroup = etsysDot1xRekeyingPairwiseGroup.setStatus('current')
etsysDot1xRekeyingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 2, 1)).setObjects(("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyingBaseGroup"), ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyingPairwiseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1xRekeyingCompliance = etsysDot1xRekeyingCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-8021X-REKEYING-MIB", PYSNMP_MODULE_ID=etsys8021xRekeyingMIB, etsysDot1xRekeyConfigTable=etsysDot1xRekeyConfigTable, etsysDot1xRekeyLength=etsysDot1xRekeyLength, etsysDot1xRekeyingPairwiseGroup=etsysDot1xRekeyingPairwiseGroup, etsysDot1xRekeyingBaseGroup=etsysDot1xRekeyingBaseGroup, etsysDot1xRekeyEnabled=etsysDot1xRekeyEnabled, etsysDot1xRekeyConfigEntry=etsysDot1xRekeyConfigEntry, etsysDot1xRekeyAsymmetric=etsysDot1xRekeyAsymmetric, etsysDot1xRekeyBaseBranch=etsysDot1xRekeyBaseBranch, etsysDot1xRekeyPeriod=etsysDot1xRekeyPeriod, etsysDot1xRekeyPairwise=etsysDot1xRekeyPairwise, etsysDot1xRekeyingGroups=etsysDot1xRekeyingGroups, etsysDot1xRekeyingObjects=etsysDot1xRekeyingObjects, etsysDot1xRekeyingConformance=etsysDot1xRekeyingConformance, etsys8021xRekeyingMIB=etsys8021xRekeyingMIB, etsysDot1xRekeyingCompliances=etsysDot1xRekeyingCompliances, etsysDot1xRekeyingCompliance=etsysDot1xRekeyingCompliance)
