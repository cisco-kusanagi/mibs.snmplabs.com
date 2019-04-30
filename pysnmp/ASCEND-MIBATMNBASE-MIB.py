#
# PySNMP MIB module ASCEND-MIBATMNBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMNBASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, Gauge32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, MibIdentifier, iso, Integer32, Counter32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Gauge32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "MibIdentifier", "iso", "Integer32", "Counter32", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibatmNbaseProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 41))
mibatmNbaseProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 41, 1), )
if mibBuilder.loadTexts: mibatmNbaseProfileTable.setStatus('mandatory')
mibatmNbaseProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMNBASE-MIB", "atmNbaseProfile-Index-o"))
if mibBuilder.loadTexts: mibatmNbaseProfileEntry.setStatus('mandatory')
atmNbaseProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 1), Integer32()).setLabel("atmNbaseProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmNbaseProfile_Index_o.setStatus('mandatory')
atmNbaseProfile_RandSeed = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 6), Integer32()).setLabel("atmNbaseProfile-RandSeed").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmNbaseProfile_RandSeed.setStatus('mandatory')
atmNbaseProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 41, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmNbaseProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmNbaseProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBATMNBASE-MIB", atmNbaseProfile_Index_o=atmNbaseProfile_Index_o, mibatmNbaseProfileEntry=mibatmNbaseProfileEntry, atmNbaseProfile_Action_o=atmNbaseProfile_Action_o, mibatmNbaseProfileTable=mibatmNbaseProfileTable, atmNbaseProfile_RandSeed=atmNbaseProfile_RandSeed, DisplayString=DisplayString, mibatmNbaseProfile=mibatmNbaseProfile)
