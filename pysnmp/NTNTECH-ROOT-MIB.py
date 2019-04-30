#
# PySNMP MIB module NTNTECH-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTNTECH-ROOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Integer32, TimeTicks, enterprises, Counter32, ModuleIdentity, iso, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Integer32", "TimeTicks", "enterprises", "Counter32", "ModuleIdentity", "iso", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntntechRootMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8059))
ntntechRootMIB.setRevisions(('1902-08-28 11:57', '1902-10-22 02:00', '1904-10-11 01:01', '1904-11-17 10:09',))
if mibBuilder.loadTexts: ntntechRootMIB.setLastUpdated('0411170200Z')
if mibBuilder.loadTexts: ntntechRootMIB.setOrganization('Paradyne Corporation')
class NtnIpAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnDefaultGateway(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnSubnetMask(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnDisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class NtnMacAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class NtnTimeTicks(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnCounter32(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnGauge32(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnTruthValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

ntntechNamingTree = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1))
ntntechChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1))
ntntechChassisConfigurationMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1))
ntntechChassisStatusMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2))
ntntechInterfaceModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2))
ntntechInterfaceModuleConfigurationMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 1))
ntntechInterfaceModuleStatusMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 2))
ntntechQoSMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 3))
ntntechNMSTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 3))
ntntechNMSTrapsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 3, 1))
ntntechSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 4))
ntntechSystemObjectsIdentifierMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 4, 1))
mibBuilder.exportSymbols("NTNTECH-ROOT-MIB", ntntechNMSTraps=ntntechNMSTraps, ntntechQoSMIB=ntntechQoSMIB, ntntechChassisStatusMIB=ntntechChassisStatusMIB, ntntechSystemObjects=ntntechSystemObjects, NtnDefaultGateway=NtnDefaultGateway, ntntechRootMIB=ntntechRootMIB, ntntechInterfaceModuleStatusMIB=ntntechInterfaceModuleStatusMIB, NtnCounter32=NtnCounter32, PYSNMP_MODULE_ID=ntntechRootMIB, ntntechChassis=ntntechChassis, NtnTimeTicks=NtnTimeTicks, NtnGauge32=NtnGauge32, ntntechNMSTrapsMIB=ntntechNMSTrapsMIB, NtnSubnetMask=NtnSubnetMask, NtnDisplayString=NtnDisplayString, ntntechInterfaceModule=ntntechInterfaceModule, NtnIpAddress=NtnIpAddress, ntntechNamingTree=ntntechNamingTree, ntntechChassisConfigurationMIB=ntntechChassisConfigurationMIB, ntntechInterfaceModuleConfigurationMIB=ntntechInterfaceModuleConfigurationMIB, ntntechSystemObjectsIdentifierMIB=ntntechSystemObjectsIdentifierMIB, NtnMacAddress=NtnMacAddress, NtnTruthValue=NtnTruthValue)
