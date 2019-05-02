#
# PySNMP MIB module BLUESOCKET-ROOT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLUESOCKET-ROOT
# Produced by pysmi-0.3.4 at Wed May  1 11:39:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, Bits, NotificationType, enterprises, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Counter32, IpAddress, Integer32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Bits", "NotificationType", "enterprises", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Counter32", "IpAddress", "Integer32", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
blueSocket = ModuleIdentity((1, 3, 6, 1, 4, 1, 9967))
if mibBuilder.loadTexts: blueSocket.setLastUpdated('200303100000Z')
if mibBuilder.loadTexts: blueSocket.setOrganization('Bluesocket Inc.')
if mibBuilder.loadTexts: blueSocket.setContactInfo(' Suresh Gandhi Bluesocket, Inc. Burlington, MA 01803 sgandhi@bluesocket.com ')
if mibBuilder.loadTexts: blueSocket.setDescription('This MIB is DRAFT-ONLY and is subject to change. Management Information Base for Blueserver.')
mibBuilder.exportSymbols("BLUESOCKET-ROOT", blueSocket=blueSocket, PYSNMP_MODULE_ID=blueSocket)
