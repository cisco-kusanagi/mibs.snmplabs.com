#
# PySNMP MIB module ASCEND-MIBATMNBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMNBASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, NotificationType, Counter32, Gauge32, TimeTicks, ModuleIdentity, Unsigned32, MibIdentifier, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "NotificationType", "Counter32", "Gauge32", "TimeTicks", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibatmNbaseProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 41))
mibatmNbaseProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 41, 1), )
if mibBuilder.loadTexts: mibatmNbaseProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmNbaseProfileTable.setDescription('A list of mibatmNbaseProfile profile entries.')
mibatmNbaseProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMNBASE-MIB", "atmNbaseProfile-Index-o"))
if mibBuilder.loadTexts: mibatmNbaseProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmNbaseProfileEntry.setDescription('A mibatmNbaseProfile entry containing objects that maps to the parameters of mibatmNbaseProfile profile.')
atmNbaseProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 1), Integer32()).setLabel("atmNbaseProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmNbaseProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: atmNbaseProfile_Index_o.setDescription('')
atmNbaseProfile_RandSeed = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 6), Integer32()).setLabel("atmNbaseProfile-RandSeed").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmNbaseProfile_RandSeed.setStatus('mandatory')
if mibBuilder.loadTexts: atmNbaseProfile_RandSeed.setDescription('Seed for random number generator')
atmNbaseProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmNbaseProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmNbaseProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: atmNbaseProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBATMNBASE-MIB", DisplayString=DisplayString, mibatmNbaseProfile=mibatmNbaseProfile, atmNbaseProfile_Action_o=atmNbaseProfile_Action_o, atmNbaseProfile_Index_o=atmNbaseProfile_Index_o, mibatmNbaseProfileTable=mibatmNbaseProfileTable, atmNbaseProfile_RandSeed=atmNbaseProfile_RandSeed, mibatmNbaseProfileEntry=mibatmNbaseProfileEntry)
