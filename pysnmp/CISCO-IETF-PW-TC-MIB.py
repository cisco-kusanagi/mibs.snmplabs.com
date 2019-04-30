#
# PySNMP MIB module CISCO-IETF-PW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:34:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, NotificationType, Gauge32, Bits, ObjectIdentity, iso, Integer32, TimeTicks, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "NotificationType", "Gauge32", "Bits", "ObjectIdentity", "iso", "Integer32", "TimeTicks", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpwTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 20000, 1))
cpwTCMIB.setRevisions(('2006-07-21 12:00', '2003-02-26 12:00', '2002-05-28 12:00', '2002-01-30 12:00', '2001-12-20 12:00', '2001-07-12 12:00',))
if mibBuilder.loadTexts: cpwTCMIB.setLastUpdated('200607211200Z')
if mibBuilder.loadTexts: cpwTCMIB.setOrganization('Cisco Systems, Inc.')
cpwMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 20000))
class CpwGroupID(TextualConvention, Unsigned32):
    status = 'current'

class CpwVcIDType(TextualConvention, Unsigned32):
    status = 'current'

class CpwVcIndexType(TextualConvention, Unsigned32):
    status = 'current'

class CpwVcVlanCfg(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4097)

class CpwOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class CpwVcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("other", 0), ("frameRelay", 1), ("atmAal5Vcc", 2), ("atmTransparent", 3), ("ethernetVLAN", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cep", 8), ("atmVccCell", 9), ("atmVpcCell", 10), ("ethernetVPLS", 11), ("e1Satop", 12), ("t1Satop", 13), ("e3Satop", 14), ("t3Satop", 15), ("basicCesPsn", 16), ("basicTdmIp", 17), ("tdmCasCesPsn", 18), ("tdmCasTdmIp", 19))

mibBuilder.exportSymbols("CISCO-IETF-PW-TC-MIB", CpwVcIndexType=CpwVcIndexType, cpwTCMIB=cpwTCMIB, CpwOperStatus=CpwOperStatus, CpwVcIDType=CpwVcIDType, CpwGroupID=CpwGroupID, cpwMIB=cpwMIB, CpwVcVlanCfg=CpwVcVlanCfg, CpwVcType=CpwVcType, PYSNMP_MODULE_ID=cpwTCMIB)
