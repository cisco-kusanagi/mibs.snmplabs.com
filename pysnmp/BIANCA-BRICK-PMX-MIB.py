#
# PySNMP MIB module BIANCA-BRICK-PMX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-PMX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Bits, Unsigned32, ObjectIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter64, Gauge32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Bits", "Unsigned32", "ObjectIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter64", "Gauge32", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
pmx = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 12))
class Date(Integer32):
    pass

class HexValue(Integer32):
    pass

pmxIfTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 12, 1), )
if mibBuilder.loadTexts: pmxIfTable.setStatus('mandatory')
pmxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-PMX-MIB", "pmxIfIndex"))
if mibBuilder.loadTexts: pmxIfEntry.setStatus('mandatory')
pmxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfIndex.setStatus('mandatory')
pmxIfSelftest = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("successful", 1), ("acfa-failure", 2), ("m32-failure", 3), ("mem-failure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfSelftest.setStatus('mandatory')
pmxIfLayer1State = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("active", 1), ("remote-alarm", 2), ("no-signal", 3), ("no-sync", 4), ("crc-error", 5), ("power-on", 6), ("resync", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmxIfLayer1State.setStatus('mandatory')
pmxIfLayer1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("e1", 1), ("t1", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfLayer1Mode.setStatus('mandatory')
pmxIfLayer1Framing = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("e1", 1), ("e1-mf", 2), ("e1-crc", 3), ("e1-mf-crc", 4), ("t1-esf", 5), ("t1-d4", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmxIfLayer1Framing.setStatus('mandatory')
pmxIfLayer1LineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("e1-hdb3", 1), ("t1-b8zs", 2), ("t1-ami", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmxIfLayer1LineCode.setStatus('mandatory')
pmxIfChannelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("e1-standard", 1), ("e1-1tr6", 2), ("e1-H0", 3), ("e1-H12", 4), ("e1-burst", 5), ("e1-raw", 6), ("t1-standard", 10), ("t1-H0", 11), ("t1-H11", 12), ("t1-burst", 13), ("t1-raw", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmxIfChannelMode.setStatus('mandatory')
pmxIfLoopbackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-loop", 1), ("full-loop", 2), ("all-channels", 3), ("only-bchannels", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmxIfLoopbackMode.setStatus('mandatory')
pmxIfErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfErrors.setStatus('mandatory')
pmxIfPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("go-thru", 2), ("go-thru-tst", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmxIfPortMode.setStatus('mandatory')
pmxIfLOS = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfLOS.setStatus('mandatory')
pmxIfNoFAS = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfNoFAS.setStatus('mandatory')
pmxIfRemoteAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfRemoteAlarms.setStatus('mandatory')
pmxIfAlarmInds = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfAlarmInds.setStatus('mandatory')
pmxIfCRC4Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfCRC4Errors.setStatus('mandatory')
pmxIfSlipPositive = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfSlipPositive.setStatus('mandatory')
pmxIfSlipNegative = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 12, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmxIfSlipNegative.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-PMX-MIB", pmxIfLayer1Mode=pmxIfLayer1Mode, bibo=bibo, dod=dod, pmxIfNoFAS=pmxIfNoFAS, pmxIfSlipPositive=pmxIfSlipPositive, pmxIfLayer1LineCode=pmxIfLayer1LineCode, pmxIfSelftest=pmxIfSelftest, org=org, pmxIfLoopbackMode=pmxIfLoopbackMode, pmxIfSlipNegative=pmxIfSlipNegative, pmxIfChannelMode=pmxIfChannelMode, Date=Date, pmxIfLayer1State=pmxIfLayer1State, pmxIfTable=pmxIfTable, pmxIfEntry=pmxIfEntry, pmxIfRemoteAlarms=pmxIfRemoteAlarms, pmxIfErrors=pmxIfErrors, pmxIfLayer1Framing=pmxIfLayer1Framing, HexValue=HexValue, pmxIfAlarmInds=pmxIfAlarmInds, pmxIfPortMode=pmxIfPortMode, internet=internet, pmxIfLOS=pmxIfLOS, enterprises=enterprises, pmxIfCRC4Errors=pmxIfCRC4Errors, pmx=pmx, private=private, pmxIfIndex=pmxIfIndex, bintec=bintec)
