#
# PySNMP MIB module APPIAN-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPIAN-SMI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, iso, ObjectIdentity, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, IpAddress, Integer32, MibIdentifier, Bits, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "iso", "ObjectIdentity", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "IpAddress", "Integer32", "MibIdentifier", "Bits", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
appian = ModuleIdentity((1, 3, 6, 1, 4, 1, 2785))
appian.setRevisions(('1900-01-27 00:00',))
if mibBuilder.loadTexts: appian.setLastUpdated('0001270000Z')
if mibBuilder.loadTexts: appian.setOrganization('Appian Communications, Inc.')
class AcAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("activate", 1), ("delete", 2), ("inactivate", 3))

class AcOpStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("operational", 1), ("offline", 2), ("initializing", 3), ("selfTesting", 4), ("provisioning", 5), ("upgrading", 6), ("maintenance", 7), ("standby", 8), ("shuttingDown", 9), ("failed", 10), ("hw-not-present", 11))

class AcSlotNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 100))
    namedValues = NamedValues(("ac0", 0), ("ac1", 1), ("ac2", 2), ("ac3", 3), ("ac4", 4), ("ac5", 5), ("ac6", 6), ("ac7", 7), ("ac8", 8), ("ac9", 9), ("ac10", 10), ("ac11", 11), ("ac12", 12), ("ac13", 13), ("ac14", 14), ("ac15", 15), ("ac16", 16), ("ac100", 100))

class AcPortNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class AcLastChange(TextualConvention, TimeTicks):
    status = 'current'

class AcMibVersion(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 9)

class AcSwVersion(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 19)

class AcNodeId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class AcRingId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class AcNodeArchitecture(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unconfigured", 0), ("linear", 1), ("ring", 2), ("ring-interconnect", 3), ("drop-and-continue-pri", 4), ("drop-and-continue-sec", 5), ("subtending-pri", 6), ("subtending-sec", 7))

acIdentifier = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 1))
acProductId = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 1, 1))
acOsap = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2))
acPport = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 3))
acLport = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 4))
acTrunks = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 6))
acServices = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 8))
mibBuilder.exportSymbols("APPIAN-SMI-MIB", acTrunks=acTrunks, appian=appian, AcRingId=AcRingId, AcPortNumber=AcPortNumber, acOsap=acOsap, AcNodeArchitecture=AcNodeArchitecture, AcSlotNumber=AcSlotNumber, AcOpStatus=AcOpStatus, AcAdminStatus=AcAdminStatus, acLport=acLport, PYSNMP_MODULE_ID=appian, acServices=acServices, acIdentifier=acIdentifier, AcMibVersion=AcMibVersion, acPport=acPport, AcSwVersion=AcSwVersion, AcLastChange=AcLastChange, AcNodeId=AcNodeId, acProductId=acProductId)
