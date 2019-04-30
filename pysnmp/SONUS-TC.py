#
# PySNMP MIB module SONUS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter64, Gauge32, MibIdentifier, TimeTicks, Bits, IpAddress, ObjectIdentity, ModuleIdentity, Integer32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter64", "Gauge32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Integer32", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonusModules, = mibBuilder.importSymbols("SONUS-SMI", "sonusModules")
sonusTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 3, 1))
if mibBuilder.loadTexts: sonusTextualConventions.setLastUpdated('200107310000Z')
if mibBuilder.loadTexts: sonusTextualConventions.setOrganization('Sonus Networks, Inc.')
class HwTypeID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50))
    namedValues = NamedValues(("none", 1), ("unknown", 14), ("undefined", 15), ("mns10", 16), ("pns10", 17), ("cns10", 18), ("cns30", 19), ("mta01", 20), ("mna10", 21), ("pna10", 22), ("cna33", 23), ("cna10", 24), ("cna30", 25), ("sonicPlane", 26), ("fanTray", 27), ("mta10", 28), ("cna01", 29), ("cna03", 30), ("cns20", 31), ("pns20", 32), ("sps60", 33), ("cna20", 34), ("cna21", 35), ("pna21", 36), ("pna23", 37), ("cns61", 38), ("cna61", 39), ("mta20", 40), ("mta21", 41), ("cna06", 42), ("cns31", 43), ("cns25", 44), ("cna25", 45), ("pns30", 46), ("pna30", 47), ("sonicPlane2", 48), ("cna02", 49), ("cna05", 50))

class ServerTypeID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16, 17, 18, 19, 31, 32, 44, 43, 46, 38))
    namedValues = NamedValues(("mns10", 16), ("pns10", 17), ("cns10", 18), ("cns30", 19), ("cns20", 31), ("pns20", 32), ("cns25", 44), ("cns31", 43), ("pns30", 46), ("cns61", 38))

class AdapterTypeID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 21, 22, 24, 25, 23, 29, 30, 34, 35, 36, 45, 47, 49, 50, 39, 42))
    namedValues = NamedValues(("none", 1), ("mna10", 21), ("pna10", 22), ("cna10", 24), ("cna30", 25), ("cna33", 23), ("cna01", 29), ("cna03", 30), ("cna20", 34), ("cna21", 35), ("pna21", 36), ("cna25", 45), ("pna30", 47), ("cna02", 49), ("cna05", 50), ("cna61", 39), ("cna06", 42))

class ServerFunctionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("default", 1), ("atm", 2), ("mgmt", 3), ("t1", 4), ("e1", 5), ("t3", 6), ("sps", 7), ("oc3tdm", 8), ("pos", 9), ("enet", 10))

class SonusShelfIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 6)

class SonusSlotIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16)

class SonusEventString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '511a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 511)

class SonusEventClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("sysmgmt", 1), ("callproc", 2), ("resmgmt", 3), ("directory", 4), ("netmgmt", 5), ("signaling", 6), ("routing", 7), ("trace", 8))

class SonusEventLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("info", 4))

class SonusEventFilterLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("noevents", 0), ("critical", 1), ("major", 2), ("minor", 3), ("info", 4))

class SonusName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 23)

class SonusNameReference(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 23)

class SonusBoolean(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("false", 1), ("true", 2))

class PointCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class SonusSysId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63))
    namedValues = NamedValues(("evlog", 1), ("ncm", 2), ("nrs", 3), ("fm", 4), ("sm", 5), ("sma", 6), ("nrm", 7), ("nrma", 8), ("brm", 9), ("drm", 10), ("prm", 11), ("xrm", 12), ("cc", 13), ("icm", 14), ("ipdh", 15), ("epdh", 16), ("ds", 17), ("debug", 18), ("trm", 19), ("sg", 20), ("gwfe", 21), ("gwsg", 22), ("sg-7", 23), ("rtcp", 24), ("tccs", 25), ("cli", 26), ("snmp", 27), ("hsim", 28), ("lesim", 29), ("ss7fe", 30), ("led", 31), ("param", 32), ("cb", 33), ("acm", 34), ("ntp", 35), ("diag", 36), ("cam", 37), ("asg", 38), ("mgsg", 39), ("ipdcfe", 40), ("ltt", 41), ("tm", 42), ("stm", 43), ("sta", 44), ("nfs", 45), ("isdn", 46), ("enm", 47), ("arm", 48), ("arma", 49), ("rtm", 50), ("psdh", 51), ("atmrm", 52), ("dcl", 53), ("psd", 54), ("cassg", 55), ("pfa", 56), ("mgcpfe", 57), ("spm", 58), ("spma", 59), ("h323sg", 60), ("h323fe", 61), ("sipsg", 62), ("sipfe", 63))

class SonusServiceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("outOfService", 1), ("inService", 2))

class SonusAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class SonusAdminAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("dryUp", 1), ("force", 2))

class SonusCircuitState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unblocked", 1), ("blocked", 2), ("transientUnblock", 3), ("transientBlock", 4), ("notAvailable", 5))

class SonusMtaSlotIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mta1", 1), ("mta2", 2))

class SonusTimingSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("extClkA", 1), ("extClkB", 2), ("refClkA", 3), ("refClkB", 4), ("oscillator", 5), ("holdover", 6))

class SonusSoftwareVersion(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d.2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class SonusSystemName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SonusTrapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("trapv1", 1), ("trapv2", 2), ("inform", 3))

class SonusAccessLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("readOnly", 1), ("readWrite", 2), ("admin", 3))

class SonusPointCode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class SonusPointCodeFormat(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d-'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class SonusSupportFlag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unsupported", 1), ("supported", 2))

mibBuilder.exportSymbols("SONUS-TC", PointCode=PointCode, SonusSystemName=SonusSystemName, SonusServiceState=SonusServiceState, PYSNMP_MODULE_ID=sonusTextualConventions, ServerTypeID=ServerTypeID, SonusTrapType=SonusTrapType, SonusAdminState=SonusAdminState, SonusEventLevel=SonusEventLevel, SonusMtaSlotIndex=SonusMtaSlotIndex, SonusEventString=SonusEventString, SonusCircuitState=SonusCircuitState, SonusPointCode=SonusPointCode, SonusAccessLevel=SonusAccessLevel, SonusEventClass=SonusEventClass, SonusSupportFlag=SonusSupportFlag, SonusBoolean=SonusBoolean, SonusSlotIndex=SonusSlotIndex, sonusTextualConventions=sonusTextualConventions, HwTypeID=HwTypeID, SonusSoftwareVersion=SonusSoftwareVersion, SonusSysId=SonusSysId, ServerFunctionType=ServerFunctionType, SonusPointCodeFormat=SonusPointCodeFormat, SonusName=SonusName, SonusAdminAction=SonusAdminAction, SonusEventFilterLevel=SonusEventFilterLevel, SonusNameReference=SonusNameReference, SonusShelfIndex=SonusShelfIndex, SonusTimingSource=SonusTimingSource, AdapterTypeID=AdapterTypeID)
