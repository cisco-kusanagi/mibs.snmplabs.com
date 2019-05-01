#
# PySNMP MIB module SONUS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:09:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, ModuleIdentity, NotificationType, IpAddress, Gauge32, Counter64, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonusModules, = mibBuilder.importSymbols("SONUS-SMI", "sonusModules")
sonusTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 3, 1))
if mibBuilder.loadTexts: sonusTextualConventions.setLastUpdated('200107310000Z')
if mibBuilder.loadTexts: sonusTextualConventions.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusTextualConventions.setContactInfo(' Sonus Networks, Inc. Customer Service Postal: 5 Carlisle Rd Westford, MA 01886 USA Tel: 978-692-8999 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusTextualConventions.setDescription('This module defines textual conventions used throughout sonus enterprise mibs.')
class HwTypeID(TextualConvention, Integer32):
    description = 'Represents the different types of hardware components that are available in a GSX9000 shelf.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50))
    namedValues = NamedValues(("none", 1), ("unknown", 14), ("undefined", 15), ("mns10", 16), ("pns10", 17), ("cns10", 18), ("cns30", 19), ("mta01", 20), ("mna10", 21), ("pna10", 22), ("cna33", 23), ("cna10", 24), ("cna30", 25), ("sonicPlane", 26), ("fanTray", 27), ("mta10", 28), ("cna01", 29), ("cna03", 30), ("cns20", 31), ("pns20", 32), ("sps60", 33), ("cna20", 34), ("cna21", 35), ("pna21", 36), ("pna23", 37), ("cns61", 38), ("cna61", 39), ("mta20", 40), ("mta21", 41), ("cna06", 42), ("cns31", 43), ("cns25", 44), ("cna25", 45), ("pns30", 46), ("pna30", 47), ("sonicPlane2", 48), ("cna02", 49), ("cna05", 50))

class ServerTypeID(TextualConvention, Integer32):
    description = 'Represents the different types of server modules which are available in a GSX9000 shelf.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16, 17, 18, 19, 31, 32, 44, 43, 46, 38))
    namedValues = NamedValues(("mns10", 16), ("pns10", 17), ("cns10", 18), ("cns30", 19), ("cns20", 31), ("pns20", 32), ("cns25", 44), ("cns31", 43), ("pns30", 46), ("cns61", 38))

class AdapterTypeID(TextualConvention, Integer32):
    description = 'Represents the different types of adapter modules which are available in a GSX9000 shelf.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 21, 22, 24, 25, 23, 29, 30, 34, 35, 36, 45, 47, 49, 50, 39, 42))
    namedValues = NamedValues(("none", 1), ("mna10", 21), ("pna10", 22), ("cna10", 24), ("cna30", 25), ("cna33", 23), ("cna01", 29), ("cna03", 30), ("cna20", 34), ("cna21", 35), ("pna21", 36), ("cna25", 45), ("pna30", 47), ("cna02", 49), ("cna05", 50), ("cna61", 39), ("cna06", 42))

class ServerFunctionType(TextualConvention, Integer32):
    description = 'Represents the logical function of the server/adapter pair'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("default", 1), ("atm", 2), ("mgmt", 3), ("t1", 4), ("e1", 5), ("t3", 6), ("sps", 7), ("oc3tdm", 8), ("pos", 9), ("enet", 10))

class SonusShelfIndex(TextualConvention, Integer32):
    description = 'The index for a Sonus shelf.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 6)

class SonusSlotIndex(TextualConvention, Integer32):
    description = 'The index for a Sonus slot.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16)

class SonusEventString(TextualConvention, OctetString):
    description = 'This data type is used to model textual information taken from the NVT ASCII character set.'
    status = 'current'
    displayHint = '511a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 511)

class SonusEventClass(TextualConvention, Integer32):
    description = 'The categories of which events are classified by.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("sysmgmt", 1), ("callproc", 2), ("resmgmt", 3), ("directory", 4), ("netmgmt", 5), ("signaling", 6), ("routing", 7), ("trace", 8))

class SonusEventLevel(TextualConvention, Integer32):
    description = 'The severity level of events.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("info", 4))

class SonusEventFilterLevel(TextualConvention, Integer32):
    description = 'The filter severity level of events.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("noevents", 0), ("critical", 1), ("major", 2), ("minor", 3), ("info", 4))

class SonusName(TextualConvention, OctetString):
    description = 'This data type is used to model textual information taken from the NVT ASCII character set. The SonusName type is used to label Sonus Named objects.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 23)

class SonusNameReference(TextualConvention, OctetString):
    description = 'This data type is used to model textual information taken from the NVT ASCII character set. The SonusNameReference type is used to refer to Sonus Named objects.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 23)

class SonusBoolean(TextualConvention, Integer32):
    description = 'This data type is used to model a boolean value expressed as true or false.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("false", 1), ("true", 2))

class PointCode(TextualConvention, Integer32):
    description = 'A three octet data type representing the SS7 PointCode. The octets represent Network-Cluster-Member values respectively.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class SonusSysId(TextualConvention, Integer32):
    description = 'An INTEGER representing the sub-system identifiers for software components in a GSX9000 node.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63))
    namedValues = NamedValues(("evlog", 1), ("ncm", 2), ("nrs", 3), ("fm", 4), ("sm", 5), ("sma", 6), ("nrm", 7), ("nrma", 8), ("brm", 9), ("drm", 10), ("prm", 11), ("xrm", 12), ("cc", 13), ("icm", 14), ("ipdh", 15), ("epdh", 16), ("ds", 17), ("debug", 18), ("trm", 19), ("sg", 20), ("gwfe", 21), ("gwsg", 22), ("sg-7", 23), ("rtcp", 24), ("tccs", 25), ("cli", 26), ("snmp", 27), ("hsim", 28), ("lesim", 29), ("ss7fe", 30), ("led", 31), ("param", 32), ("cb", 33), ("acm", 34), ("ntp", 35), ("diag", 36), ("cam", 37), ("asg", 38), ("mgsg", 39), ("ipdcfe", 40), ("ltt", 41), ("tm", 42), ("stm", 43), ("sta", 44), ("nfs", 45), ("isdn", 46), ("enm", 47), ("arm", 48), ("arma", 49), ("rtm", 50), ("psdh", 51), ("atmrm", 52), ("dcl", 53), ("psd", 54), ("cassg", 55), ("pfa", 56), ("mgcpfe", 57), ("spm", 58), ("spma", 59), ("h323sg", 60), ("h323fe", 61), ("sipsg", 62), ("sipfe", 63))

class SonusServiceState(TextualConvention, Integer32):
    description = 'The service state of a resource.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("outOfService", 1), ("inService", 2))

class SonusAdminState(TextualConvention, Integer32):
    description = 'The administrative state of a resource.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class SonusAdminAction(TextualConvention, Integer32):
    description = 'The action assignment of a resource.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("dryUp", 1), ("force", 2))

class SonusCircuitState(TextualConvention, Integer32):
    description = 'The state of an ISUP circuit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unblocked", 1), ("blocked", 2), ("transientUnblock", 3), ("transientBlock", 4), ("notAvailable", 5))

class SonusMtaSlotIndex(TextualConvention, Integer32):
    description = 'The index identifying an MTA slot'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mta1", 1), ("mta2", 2))

class SonusTimingSource(TextualConvention, Integer32):
    description = 'Timing source types. extClkA and extClkB specifiy either BITS or SETS clock inputs, depending on whether the MTA is an MTA10(BITS) or MTA20(SETS). refClkA and refClkB indicate recovered/derived from a DS1 (for instance)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("extClkA", 1), ("extClkB", 2), ("refClkA", 3), ("refClkB", 4), ("oscillator", 5), ("holdover", 6))

class SonusSoftwareVersion(TextualConvention, OctetString):
    description = 'Octet string that identifies the version of the runtime software application: Byte(s) Code ------- ---- 0 major version 1 minor version 2 release version 3 type (1:alpha, 2:beta, 3:release, 4:special) 4-5 type number'
    status = 'current'
    displayHint = '1d.1d.1d.1d.2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class SonusSystemName(TextualConvention, OctetString):
    description = 'This data type refers to the name of networking device.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SonusTrapType(TextualConvention, Integer32):
    description = 'The type of trap PDU to be generated: none - no PDU is generated trapv1 - SNMPv1-Trap-PDU trapv2 - SNMPv2-Trap-PDU inform - InformRequestPDU'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("trapv1", 1), ("trapv2", 2), ("inform", 3))

class SonusAccessLevel(TextualConvention, Integer32):
    description = 'The User and Mgmt Client access level.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("readOnly", 1), ("readWrite", 2), ("admin", 3))

class SonusPointCode(TextualConvention, OctetString):
    description = 'Octet string that represents a point code. A point code may be comprised of one or more sub-values. Each sub-value is stored in two bytes of the octet string. The first two bytes of the octet string contains the count of the two-byte sub-values that comprise the point code. The remaining bytes of the octet string contain the two-byte sub-values. For example: Point Code Octet String ---------- ------------ 4-200-7 00 04 00 C8 00 07 2-1000-3 00 02 03 E8 00 08 15-750 00 FF 02 EE 16000 3E 80'
    status = 'current'
    displayHint = '2d-'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class SonusPointCodeFormat(TextualConvention, OctetString):
    description = 'Octet string that represents a point code format, such as 2-10-2, 3-8-3, 4-10 or 14. A point code format specifies the number of bits that each sub-value of a point code value is stored in. The total number of bits should be 14. A point code format is used to specify how a point code value should be stored in a 14 bit value. A point code format may be comprised of one or more numbers. Each number is stored in one byte of the octet string. The first byte of the octet string contains the count of the one-byte numbers that comprise the point code format. The remaining bytes of the octet string contain the one-byte numbers. For example: Point Code Format Octet String ----------------- ------------ 3-8-3 03 08 03 2-10-2 02 0A 02 4-10 04 0A 14 0E'
    status = 'current'
    displayHint = '1d-'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class SonusSupportFlag(TextualConvention, Integer32):
    description = 'The flag to indicate if the attribute is supported.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unsupported", 1), ("supported", 2))

mibBuilder.exportSymbols("SONUS-TC", SonusAdminAction=SonusAdminAction, ServerFunctionType=ServerFunctionType, SonusSoftwareVersion=SonusSoftwareVersion, SonusShelfIndex=SonusShelfIndex, SonusSlotIndex=SonusSlotIndex, SonusAdminState=SonusAdminState, SonusEventString=SonusEventString, SonusEventClass=SonusEventClass, SonusServiceState=SonusServiceState, HwTypeID=HwTypeID, SonusNameReference=SonusNameReference, AdapterTypeID=AdapterTypeID, SonusName=SonusName, PYSNMP_MODULE_ID=sonusTextualConventions, sonusTextualConventions=sonusTextualConventions, SonusPointCode=SonusPointCode, SonusSupportFlag=SonusSupportFlag, SonusTimingSource=SonusTimingSource, SonusBoolean=SonusBoolean, SonusAccessLevel=SonusAccessLevel, SonusEventLevel=SonusEventLevel, PointCode=PointCode, SonusPointCodeFormat=SonusPointCodeFormat, SonusMtaSlotIndex=SonusMtaSlotIndex, SonusCircuitState=SonusCircuitState, SonusEventFilterLevel=SonusEventFilterLevel, SonusSysId=SonusSysId, ServerTypeID=ServerTypeID, SonusSystemName=SonusSystemName, SonusTrapType=SonusTrapType)
