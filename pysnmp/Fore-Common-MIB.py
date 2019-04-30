#
# PySNMP MIB module Fore-Common-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Common-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:00:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ModuleIdentity, ObjectIdentity, TimeTicks, IpAddress, MibIdentifier, Bits, Counter32, enterprises, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "Counter32", "enterprises", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fore = ModuleIdentity((1, 3, 6, 1, 4, 1, 326))
if mibBuilder.loadTexts: fore.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: fore.setOrganization('Marconi Communications')
admin = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
foreExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 3))
operations = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 1))
snmpErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 2))
snmpTrapDest = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 3))
snmpAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 4))
assembly = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 5))
fileXfr = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 6))
rmonExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 7))
preDot1qVlanMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 8))
snmpTrapLog = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 9))
ilmisnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 10))
entityExtensionMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 11))
ilmiRegistry = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 14))
foreIfExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 15))
frameInternetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 16))
ifExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 17))
atmAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 1))
atmSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2))
etherSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 3))
atmAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 5))
hubSwitchRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 6))
ipoa = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 7))
stackSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 10))
switchRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 15))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 2))
asxd = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1))
hardware = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1))
asx = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1))
asx200wg = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 4))
asx200bx = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 5))
asx200bxe = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 6))
cabletron9A000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 7))
asx1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 8))
le155 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 9))
sfcs200wg = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 10))
sfcs200bx = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 11))
sfcs1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 12))
tnx210 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 15))
tnx1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 16))
asx1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 17))
asx4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 18))
le25 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 19))
esx3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 20))
tnx1100b = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 21))
asx150 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 22))
bxr48000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 24))
asx4000m = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 25))
axhIp = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 26))
axhSig = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 27))
class SpansAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class AtmAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(20, 20), )
class NsapPrefix(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(13, 13)
    fixedLength = 13

class NsapAddr(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class TransitNetwork(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 4)

class TrapNumber(Integer32):
    pass

class EntryStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4))

class AtmSigProtocol(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("spans", 2), ("q2931", 3), ("pvc", 4), ("spvc", 5), ("oam", 6), ("spvcSpans", 7), ("spvcPnni", 8), ("rcc", 9), ("fsig", 10), ("mpls", 11), ("ipCtl", 12), ("oam-ctl", 13))

class GeneralState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("fail", 2))

class IntegerBitString(Integer32):
    pass

class ConnectionType(Integer32):
    pass

mibBuilder.exportSymbols("Fore-Common-MIB", asx200wg=asx200wg, atmAccess=atmAccess, systems=systems, preDot1qVlanMIB=preDot1qVlanMIB, rmonExtensions=rmonExtensions, asx1000=asx1000, esx3000=esx3000, snmpErrors=snmpErrors, stackSwitch=stackSwitch, sfcs200bx=sfcs200bx, software=software, cabletron9A000=cabletron9A000, EntryStatus=EntryStatus, asx4000=asx4000, axhIp=axhIp, operations=operations, snmpTrapDest=snmpTrapDest, entityExtensionMIB=entityExtensionMIB, AtmSigProtocol=AtmSigProtocol, sfcs200wg=sfcs200wg, ipoa=ipoa, hubSwitchRouter=hubSwitchRouter, etherSwitch=etherSwitch, axhSig=axhSig, le155=le155, ConnectionType=ConnectionType, ilmisnmp=ilmisnmp, fore=fore, frameInternetworking=frameInternetworking, snmpTrapLog=snmpTrapLog, foreIfExtension=foreIfExtension, bxr48000=bxr48000, tnx210=tnx210, switchRouter=switchRouter, atmSwitch=atmSwitch, asx200bx=asx200bx, asxd=asxd, asx=asx, snmpAccess=snmpAccess, SpansAddress=SpansAddress, IntegerBitString=IntegerBitString, PYSNMP_MODULE_ID=fore, sfcs1000=sfcs1000, NsapPrefix=NsapPrefix, asx4000m=asx4000m, ifExtensions=ifExtensions, asx150=asx150, AtmAddress=AtmAddress, fileXfr=fileXfr, foreExperiment=foreExperiment, assembly=assembly, tnx1100=tnx1100, asx1200=asx1200, tnx1100b=tnx1100b, NsapAddr=NsapAddr, ilmiRegistry=ilmiRegistry, hardware=hardware, asx200bxe=asx200bxe, TrapNumber=TrapNumber, atmAdapter=atmAdapter, GeneralState=GeneralState, TransitNetwork=TransitNetwork, admin=admin, le25=le25)
