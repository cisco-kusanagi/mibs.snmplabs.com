#
# PySNMP MIB module ASCEND-MIBPERDNIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBPERDNIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, ModuleIdentity, IpAddress, iso, Unsigned32, TimeTicks, MibIdentifier, Counter64, NotificationType, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "ModuleIdentity", "IpAddress", "iso", "Unsigned32", "TimeTicks", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibperDnisProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 100))
mibperDnisProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 100, 1), )
if mibBuilder.loadTexts: mibperDnisProfileTable.setStatus('mandatory')
mibperDnisProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1), ).setIndexNames((0, "ASCEND-MIBPERDNIS-MIB", "perDnisProfile-DialedNumber"))
if mibBuilder.loadTexts: mibperDnisProfileEntry.setStatus('mandatory')
perDnisProfile_DialedNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 1), DisplayString()).setLabel("perDnisProfile-DialedNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: perDnisProfile_DialedNumber.setStatus('mandatory')
perDnisProfile_CallType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("digital", 1), ("voice", 2)))).setLabel("perDnisProfile-CallType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: perDnisProfile_CallType.setStatus('mandatory')
perDnisProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("perDnisProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: perDnisProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBPERDNIS-MIB", mibperDnisProfileTable=mibperDnisProfileTable, perDnisProfile_Action_o=perDnisProfile_Action_o, perDnisProfile_CallType=perDnisProfile_CallType, mibperDnisProfile=mibperDnisProfile, perDnisProfile_DialedNumber=perDnisProfile_DialedNumber, DisplayString=DisplayString, mibperDnisProfileEntry=mibperDnisProfileEntry)
