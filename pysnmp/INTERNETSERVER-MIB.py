#
# PySNMP MIB module INTERNETSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/INTERNETSERVER-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:31:09 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
software, microsoft = mibBuilder.importSymbols("MSFT-MIB", "software", "microsoft")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, iso, enterprises, Gauge32, NotificationType, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Integer32, MibIdentifier, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "iso", "enterprises", "Gauge32", "NotificationType", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Integer32", "MibIdentifier", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
internetServer = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 7))
inetSrvCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 7, 1))
inetSrvStats = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 7, 1, 1))
mibBuilder.exportSymbols("INTERNETSERVER-MIB", inetSrvStats=inetSrvStats, inetSrvCommon=inetSrvCommon, internetServer=internetServer)
