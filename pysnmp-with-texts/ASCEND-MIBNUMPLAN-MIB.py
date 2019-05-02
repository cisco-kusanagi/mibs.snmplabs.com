#
# PySNMP MIB module ASCEND-MIBNUMPLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBNUMPLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, Bits, Counter64, ObjectIdentity, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, iso, NotificationType, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Bits", "Counter64", "ObjectIdentity", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "iso", "NotificationType", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibnumberPlanProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 96))
mibnumberPlanProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 96, 1), )
if mibBuilder.loadTexts: mibnumberPlanProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibnumberPlanProfileTable.setDescription('A list of mibnumberPlanProfile profile entries.')
mibnumberPlanProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1), ).setIndexNames((0, "ASCEND-MIBNUMPLAN-MIB", "numberPlanProfile-Name"))
if mibBuilder.loadTexts: mibnumberPlanProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibnumberPlanProfileEntry.setDescription('A mibnumberPlanProfile entry containing objects that maps to the parameters of mibnumberPlanProfile profile.')
numberPlanProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 1), DisplayString()).setLabel("numberPlanProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: numberPlanProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: numberPlanProfile_Name.setDescription('')
numberPlanProfile_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("numberPlanProfile-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberPlanProfile_Active.setStatus('mandatory')
if mibBuilder.loadTexts: numberPlanProfile_Active.setDescription('TRUE to allow use of this prefix, FALSE otherwise.')
numberPlanProfile_DialPrefix = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 3), DisplayString()).setLabel("numberPlanProfile-DialPrefix").setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberPlanProfile_DialPrefix.setStatus('mandatory')
if mibBuilder.loadTexts: numberPlanProfile_DialPrefix.setDescription('Dial prefix to match.')
numberPlanProfile_NumDigits = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 4), Integer32()).setLabel("numberPlanProfile-NumDigits").setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberPlanProfile_NumDigits.setStatus('mandatory')
if mibBuilder.loadTexts: numberPlanProfile_NumDigits.setDescription('Number of digits in a phone number matching the associated dial prefix.')
numberPlanProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("numberPlanProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberPlanProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: numberPlanProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBNUMPLAN-MIB", numberPlanProfile_DialPrefix=numberPlanProfile_DialPrefix, numberPlanProfile_Name=numberPlanProfile_Name, mibnumberPlanProfileEntry=mibnumberPlanProfileEntry, DisplayString=DisplayString, numberPlanProfile_Active=numberPlanProfile_Active, mibnumberPlanProfileTable=mibnumberPlanProfileTable, numberPlanProfile_NumDigits=numberPlanProfile_NumDigits, mibnumberPlanProfile=mibnumberPlanProfile, numberPlanProfile_Action_o=numberPlanProfile_Action_o)
