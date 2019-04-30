#
# PySNMP MIB module A3COM0034-PROBECONFIG-EXTENSION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0034-PROBECONFIG-EXTENSION
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
probeConfigNetExtensions, = mibBuilder.importSymbols("A3COM0027-RMON-EXTENSIONS", "probeConfigNetExtensions")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, iso, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, ObjectIdentity, IpAddress, Counter32, Bits, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "iso", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "ObjectIdentity", "IpAddress", "Counter32", "Bits", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extNetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 25, 6, 1), )
if mibBuilder.loadTexts: extNetConfigTable.setStatus('mandatory')
extNetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 25, 6, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extNetConfigEntry.setStatus('mandatory')
extNetConfigDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 6, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extNetConfigDefaultGateway.setStatus('mandatory')
extNetConfigBootP = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extNetConfigBootP.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM0034-PROBECONFIG-EXTENSION", extNetConfigBootP=extNetConfigBootP, extNetConfigEntry=extNetConfigEntry, extNetConfigDefaultGateway=extNetConfigDefaultGateway, extNetConfigTable=extNetConfigTable)
