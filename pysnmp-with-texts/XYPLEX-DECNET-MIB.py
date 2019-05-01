#
# PySNMP MIB module XYPLEX-DECNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYPLEX-DECNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:46:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("RFC1212-CONCISE-MIB", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, TimeTicks, Counter32, ObjectIdentity, Counter64, ModuleIdentity, iso, Integer32, enterprises, Unsigned32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "TimeTicks", "Counter32", "ObjectIdentity", "Counter64", "ModuleIdentity", "iso", "Integer32", "enterprises", "Unsigned32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xyplex = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
decnet = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 14))
rcp = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 14, 1))
rcpRemoteAddress = MibScalar((1, 3, 6, 1, 4, 1, 33, 14, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcpRemoteAddress.setStatus('mandatory')
if mibBuilder.loadTexts: rcpRemoteAddress.setDescription('If a remote console session exists, the Ethernet address of the remote partner, otherwise zero length.')
mibBuilder.exportSymbols("XYPLEX-DECNET-MIB", rcpRemoteAddress=rcpRemoteAddress, decnet=decnet, rcp=rcp, xyplex=xyplex)
