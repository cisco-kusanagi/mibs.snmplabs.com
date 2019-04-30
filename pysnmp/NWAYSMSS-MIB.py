#
# PySNMP MIB module NWAYSMSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NWAYSMSS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Unsigned32, IpAddress, MibIdentifier, Gauge32, NotificationType, enterprises, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Unsigned32", "IpAddress", "MibIdentifier", "Gauge32", "NotificationType", "enterprises", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("NWAYSMSS-MIB", mssCommonHWVPD=mssCommonHWVPD, mssCmnClnts=mssCmnClnts, ibmProd=ibmProd, mssCommon=mssCommon, AtmPrivateAddrEsi=AtmPrivateAddrEsi, nwaysMSS=nwaysMSS, ibm=ibm, Bandwidth=Bandwidth, AtmSelector=AtmSelector, AtmVccTrafficType=AtmVccTrafficType, mssCmnSrvrs=mssCmnSrvrs, mssServerLanE=mssServerLanE)
