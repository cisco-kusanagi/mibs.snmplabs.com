#
# PySNMP MIB module ASCEND-MIBSHASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSHASH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Counter32, IpAddress, ModuleIdentity, Gauge32, Unsigned32, Counter64, Bits, NotificationType, ObjectIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Counter32", "IpAddress", "ModuleIdentity", "Gauge32", "Unsigned32", "Counter64", "Bits", "NotificationType", "ObjectIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibsHashProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 108))
mibsHashProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 108, 1), )
if mibBuilder.loadTexts: mibsHashProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibsHashProfileTable.setDescription('A list of mibsHashProfile profile entries.')
mibsHashProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1), ).setIndexNames((0, "ASCEND-MIBSHASH-MIB", "sHashProfile-Index-o"))
if mibBuilder.loadTexts: mibsHashProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibsHashProfileEntry.setDescription('A mibsHashProfile entry containing objects that maps to the parameters of mibsHashProfile profile.')
sHashProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 1), Integer32()).setLabel("sHashProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: sHashProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: sHashProfile_Index_o.setDescription('')
sHashProfile_Ipsec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 2), DisplayString()).setLabel("sHashProfile-Ipsec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sHashProfile_Ipsec.setStatus('mandatory')
if mibBuilder.loadTexts: sHashProfile_Ipsec.setDescription('IP Security hash code')
sHashProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("sHashProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sHashProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: sHashProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBSHASH-MIB", DisplayString=DisplayString, mibsHashProfile=mibsHashProfile, sHashProfile_Action_o=sHashProfile_Action_o, sHashProfile_Index_o=sHashProfile_Index_o, mibsHashProfileTable=mibsHashProfileTable, mibsHashProfileEntry=mibsHashProfileEntry, sHashProfile_Ipsec=sHashProfile_Ipsec)
