#
# PySNMP MIB module CISCO-MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MPLS-TC-EXT-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, MibIdentifier, Bits, Counter32, ObjectIdentity, IpAddress, Counter64, iso, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "MibIdentifier", "Bits", "Counter32", "ObjectIdentity", "IpAddress", "Counter64", "iso", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmplsTcExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 144))
cmplsTcExtStdMIB.setRevisions(('2012-02-22 00:00',))
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setLastUpdated('201202220000Z')
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
class CMplsGlobalId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CMplsNodeId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class CMplsIccId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 6)

class CMplsLocalId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16777215)

mibBuilder.exportSymbols("CISCO-MPLS-TC-EXT-STD-MIB", CMplsNodeId=CMplsNodeId, cmplsTcExtStdMIB=cmplsTcExtStdMIB, PYSNMP_MODULE_ID=cmplsTcExtStdMIB, CMplsIccId=CMplsIccId, CMplsGlobalId=CMplsGlobalId, CMplsLocalId=CMplsLocalId)
