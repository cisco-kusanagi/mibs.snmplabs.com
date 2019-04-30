#
# PySNMP MIB module ASCEND-MIBREDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBREDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Gauge32, Unsigned32, Integer32, TimeTicks, NotificationType, MibIdentifier, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Unsigned32", "Integer32", "TimeTicks", "NotificationType", "MibIdentifier", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibredundancyProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 16))
mibredundancyProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 16, 1), )
if mibBuilder.loadTexts: mibredundancyProfileTable.setStatus('mandatory')
mibredundancyProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1), ).setIndexNames((0, "ASCEND-MIBREDUNDANCY-MIB", "redundancyProfile-Index-o"))
if mibBuilder.loadTexts: mibredundancyProfileEntry.setStatus('mandatory')
redundancyProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1, 1), Integer32()).setLabel("redundancyProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyProfile_Index_o.setStatus('mandatory')
redundancyProfile_PrimaryPreference = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noPreference", 1), ("leftControllerPreferred", 2), ("rightControllerPreferred", 3), ("firstControllerPreferred", 4), ("secondControllerPreferred", 5)))).setLabel("redundancyProfile-PrimaryPreference").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redundancyProfile_PrimaryPreference.setStatus('mandatory')
redundancyProfile_SyncEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("redundancyProfile-SyncEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redundancyProfile_SyncEnabled.setStatus('mandatory')
redundancyProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("redundancyProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redundancyProfile_Action_o.setStatus('mandatory')
mibredundancyProfile_ContextTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 16, 2), ).setLabel("mibredundancyProfile-ContextTable")
if mibBuilder.loadTexts: mibredundancyProfile_ContextTable.setStatus('mandatory')
mibredundancyProfile_ContextEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 16, 2, 1), ).setLabel("mibredundancyProfile-ContextEntry").setIndexNames((0, "ASCEND-MIBREDUNDANCY-MIB", "redundancyProfile-Context-Index-o"), (0, "ASCEND-MIBREDUNDANCY-MIB", "redundancyProfile-Context-Index1-o"))
if mibBuilder.loadTexts: mibredundancyProfile_ContextEntry.setStatus('mandatory')
redundancyProfile_Context_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 16, 2, 1, 1), Integer32()).setLabel("redundancyProfile-Context-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyProfile_Context_Index_o.setStatus('mandatory')
redundancyProfile_Context_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 16, 2, 1, 2), Integer32()).setLabel("redundancyProfile-Context-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyProfile_Context_Index1_o.setStatus('mandatory')
redundancyProfile_Context_MustAgree = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 16, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("redundancyProfile-Context-MustAgree").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redundancyProfile_Context_MustAgree.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBREDUNDANCY-MIB", redundancyProfile_PrimaryPreference=redundancyProfile_PrimaryPreference, DisplayString=DisplayString, redundancyProfile_Context_Index1_o=redundancyProfile_Context_Index1_o, redundancyProfile_Index_o=redundancyProfile_Index_o, mibredundancyProfileEntry=mibredundancyProfileEntry, redundancyProfile_Action_o=redundancyProfile_Action_o, mibredundancyProfileTable=mibredundancyProfileTable, redundancyProfile_SyncEnabled=redundancyProfile_SyncEnabled, mibredundancyProfile_ContextEntry=mibredundancyProfile_ContextEntry, redundancyProfile_Context_Index_o=redundancyProfile_Context_Index_o, mibredundancyProfile=mibredundancyProfile, redundancyProfile_Context_MustAgree=redundancyProfile_Context_MustAgree, mibredundancyProfile_ContextTable=mibredundancyProfile_ContextTable)
