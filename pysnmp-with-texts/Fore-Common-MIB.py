#
# PySNMP MIB module Fore-Common-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Common-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibIdentifier, enterprises, Counter64, Unsigned32, ModuleIdentity, Counter32, TimeTicks, NotificationType, ObjectIdentity, IpAddress, Gauge32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "enterprises", "Counter64", "Unsigned32", "ModuleIdentity", "Counter32", "TimeTicks", "NotificationType", "ObjectIdentity", "IpAddress", "Gauge32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fore = ModuleIdentity((1, 3, 6, 1, 4, 1, 326))
if mibBuilder.loadTexts: fore.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: fore.setOrganization('Marconi Communications')
if mibBuilder.loadTexts: fore.setContactInfo(' Postal: Marconi Communications, Inc. 5000 Marconi Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6999 Email: bbrs-mibs@marconi.com Web: http://www.marconi.com')
if mibBuilder.loadTexts: fore.setDescription('Definitions common to all FORE private MIBS.')
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

mibBuilder.exportSymbols("Fore-Common-MIB", ilmiRegistry=ilmiRegistry, fore=fore, ilmisnmp=ilmisnmp, NsapPrefix=NsapPrefix, atmAccess=atmAccess, snmpTrapDest=snmpTrapDest, rmonExtensions=rmonExtensions, preDot1qVlanMIB=preDot1qVlanMIB, operations=operations, ipoa=ipoa, software=software, tnx1100=tnx1100, snmpErrors=snmpErrors, sfcs200bx=sfcs200bx, snmpAccess=snmpAccess, sfcs200wg=sfcs200wg, le25=le25, sfcs1000=sfcs1000, esx3000=esx3000, frameInternetworking=frameInternetworking, asx4000m=asx4000m, AtmAddress=AtmAddress, assembly=assembly, ConnectionType=ConnectionType, axhIp=axhIp, bxr48000=bxr48000, ifExtensions=ifExtensions, asx=asx, asxd=asxd, asx4000=asx4000, TransitNetwork=TransitNetwork, fileXfr=fileXfr, EntryStatus=EntryStatus, foreIfExtension=foreIfExtension, asx1000=asx1000, asx200bxe=asx200bxe, axhSig=axhSig, TrapNumber=TrapNumber, SpansAddress=SpansAddress, IntegerBitString=IntegerBitString, atmSwitch=atmSwitch, cabletron9A000=cabletron9A000, AtmSigProtocol=AtmSigProtocol, tnx1100b=tnx1100b, asx200bx=asx200bx, etherSwitch=etherSwitch, asx1200=asx1200, hubSwitchRouter=hubSwitchRouter, entityExtensionMIB=entityExtensionMIB, switchRouter=switchRouter, NsapAddr=NsapAddr, asx200wg=asx200wg, systems=systems, atmAdapter=atmAdapter, foreExperiment=foreExperiment, PYSNMP_MODULE_ID=fore, admin=admin, le155=le155, GeneralState=GeneralState, hardware=hardware, stackSwitch=stackSwitch, asx150=asx150, tnx210=tnx210, snmpTrapLog=snmpTrapLog)
