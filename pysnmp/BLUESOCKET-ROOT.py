#
# PySNMP MIB module BLUESOCKET-ROOT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLUESOCKET-ROOT
# Produced by pysmi-0.3.4 at Mon Apr 29 17:22:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, Counter64, enterprises, NotificationType, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks, Unsigned32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Counter64", "enterprises", "NotificationType", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Unsigned32", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
blueSocket = ModuleIdentity((1, 3, 6, 1, 4, 1, 9967))
if mibBuilder.loadTexts: blueSocket.setLastUpdated('200303100000Z')
if mibBuilder.loadTexts: blueSocket.setOrganization('Bluesocket Inc.')
mibBuilder.exportSymbols("BLUESOCKET-ROOT", blueSocket=blueSocket, PYSNMP_MODULE_ID=blueSocket)
