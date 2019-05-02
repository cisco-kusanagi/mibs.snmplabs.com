#
# PySNMP MIB module NWAYSMSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NWAYSMSS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, enterprises, Bits, ModuleIdentity, ObjectIdentity, Unsigned32, NotificationType, Gauge32, IpAddress, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "enterprises", "Bits", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "IpAddress", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nwaysMSS = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118))
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
mssCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1))
mssCommonHWVPD = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 1))
mssCmnSrvrs = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2))
mssServerLanE = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1))
mssCmnClnts = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 3))
class AtmPrivateAddrEsi(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class AtmSelector(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class AtmVccTrafficType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bestEffort", 1), ("reservedBandwidth", 2))

class Bandwidth(Integer32):
    pass

mibBuilder.exportSymbols("NWAYSMSS-MIB", AtmVccTrafficType=AtmVccTrafficType, mssCommon=mssCommon, ibmProd=ibmProd, AtmSelector=AtmSelector, ibm=ibm, mssServerLanE=mssServerLanE, AtmPrivateAddrEsi=AtmPrivateAddrEsi, Bandwidth=Bandwidth, mssCmnSrvrs=mssCmnSrvrs, nwaysMSS=nwaysMSS, mssCommonHWVPD=mssCommonHWVPD, mssCmnClnts=mssCmnClnts)
