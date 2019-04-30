#
# PySNMP MIB module ASCEND-MIBCLTMACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBCLTMACCESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, MibIdentifier, TimeTicks, Unsigned32, iso, Counter32, IpAddress, Counter64, ModuleIdentity, Integer32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "Unsigned32", "iso", "Counter32", "IpAddress", "Counter64", "ModuleIdentity", "Integer32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibcltmAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 67))
mibcltmAccessTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 67, 1), )
if mibBuilder.loadTexts: mibcltmAccessTable.setStatus('mandatory')
mibcltmAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1), ).setIndexNames((0, "ASCEND-MIBCLTMACCESS-MIB", "cltmAccess-Index-o"))
if mibBuilder.loadTexts: mibcltmAccessEntry.setStatus('mandatory')
cltmAccess_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 1), Integer32()).setLabel("cltmAccess-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: cltmAccess_Index_o.setStatus('mandatory')
cltmAccess_CltmSlot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17)))).setLabel("cltmAccess-CltmSlot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmAccess_CltmSlot.setStatus('mandatory')
cltmAccess_AccessSlot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17)))).setLabel("cltmAccess-AccessSlot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmAccess_AccessSlot.setStatus('mandatory')
cltmAccess_AccessPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 4), Integer32()).setLabel("cltmAccess-AccessPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmAccess_AccessPort.setStatus('mandatory')
cltmAccess_AccessLoop = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 10), Integer32()).setLabel("cltmAccess-AccessLoop").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmAccess_AccessLoop.setStatus('mandatory')
cltmAccess_AccessMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lookingOut", 1), ("bridged", 2)))).setLabel("cltmAccess-AccessMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmAccess_AccessMode.setStatus('mandatory')
cltmAccess_AccessTerminal = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("internalTesterTerminal", 1), ("externalTesterTerminal", 2), ("auxiliaryTesterTerminal", 3), ("externalLoop", 4)))).setLabel("cltmAccess-AccessTerminal").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmAccess_AccessTerminal.setStatus('mandatory')
cltmAccess_ActivateAccess = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("cltmAccess-ActivateAccess").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmAccess_ActivateAccess.setStatus('mandatory')
cltmAccess_AccessResult = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("accessActivated", 2), ("resourceBusy", 3)))).setLabel("cltmAccess-AccessResult").setMaxAccess("readonly")
if mibBuilder.loadTexts: cltmAccess_AccessResult.setStatus('mandatory')
cltmAccess_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("cltmAccess-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmAccess_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBCLTMACCESS-MIB", cltmAccess_AccessLoop=cltmAccess_AccessLoop, cltmAccess_AccessSlot=cltmAccess_AccessSlot, cltmAccess_AccessTerminal=cltmAccess_AccessTerminal, cltmAccess_ActivateAccess=cltmAccess_ActivateAccess, mibcltmAccess=mibcltmAccess, cltmAccess_AccessResult=cltmAccess_AccessResult, cltmAccess_AccessPort=cltmAccess_AccessPort, cltmAccess_Action_o=cltmAccess_Action_o, mibcltmAccessEntry=mibcltmAccessEntry, mibcltmAccessTable=mibcltmAccessTable, DisplayString=DisplayString, cltmAccess_CltmSlot=cltmAccess_CltmSlot, cltmAccess_AccessMode=cltmAccess_AccessMode, cltmAccess_Index_o=cltmAccess_Index_o)
