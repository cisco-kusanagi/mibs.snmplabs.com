#
# PySNMP MIB module ASCEND-MIBPERDNIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBPERDNIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, iso, Bits, NotificationType, ModuleIdentity, Counter32, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "iso", "Bits", "NotificationType", "ModuleIdentity", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibperDnisProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 100))
mibperDnisProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 100, 1), )
if mibBuilder.loadTexts: mibperDnisProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibperDnisProfileTable.setDescription('A list of mibperDnisProfile profile entries.')
mibperDnisProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1), ).setIndexNames((0, "ASCEND-MIBPERDNIS-MIB", "perDnisProfile-DialedNumber"))
if mibBuilder.loadTexts: mibperDnisProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibperDnisProfileEntry.setDescription('A mibperDnisProfile entry containing objects that maps to the parameters of mibperDnisProfile profile.')
perDnisProfile_DialedNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 1), DisplayString()).setLabel("perDnisProfile-DialedNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: perDnisProfile_DialedNumber.setStatus('mandatory')
if mibBuilder.loadTexts: perDnisProfile_DialedNumber.setDescription('The number dialed. Used to select how to initialize parameters for the incoming call.')
perDnisProfile_CallType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("digital", 1), ("voice", 2)))).setLabel("perDnisProfile-CallType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: perDnisProfile_CallType.setStatus('mandatory')
if mibBuilder.loadTexts: perDnisProfile_CallType.setDescription('Forces this particular call type for inband/R1/R2 incoming calls matching the DNIS of this profile.')
perDnisProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("perDnisProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: perDnisProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: perDnisProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBPERDNIS-MIB", perDnisProfile_Action_o=perDnisProfile_Action_o, mibperDnisProfileEntry=mibperDnisProfileEntry, perDnisProfile_CallType=perDnisProfile_CallType, perDnisProfile_DialedNumber=perDnisProfile_DialedNumber, DisplayString=DisplayString, mibperDnisProfileTable=mibperDnisProfileTable, mibperDnisProfile=mibperDnisProfile)
