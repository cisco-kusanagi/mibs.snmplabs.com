#
# PySNMP MIB module A3COM0034-PROBECONFIG-EXTENSION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0034-PROBECONFIG-EXTENSION
# Produced by pysmi-0.3.4 at Wed May  1 11:08:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
probeConfigNetExtensions, = mibBuilder.importSymbols("A3COM0027-RMON-EXTENSIONS", "probeConfigNetExtensions")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, Gauge32, MibIdentifier, Bits, NotificationType, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ObjectIdentity, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "MibIdentifier", "Bits", "NotificationType", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ObjectIdentity", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extNetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 25, 6, 1), )
if mibBuilder.loadTexts: extNetConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: extNetConfigTable.setDescription('A table augmenting the netConfigEntries defined in RFCxxxx.')
extNetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 25, 6, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extNetConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: extNetConfigEntry.setDescription('A set of configuration parameters for a particular network interface on this device. If the device has no network interface, this table is empty. The index is composed of the ifIndex assigned to the corresponding interface.')
extNetConfigDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 6, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extNetConfigDefaultGateway.setStatus('mandatory')
if mibBuilder.loadTexts: extNetConfigDefaultGateway.setDescription('The IP Address of the default gateway. If this value is undefined or unknown, it shall have the value 0.0.0.0.')
extNetConfigBootP = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extNetConfigBootP.setStatus('mandatory')
if mibBuilder.loadTexts: extNetConfigBootP.setDescription('This parameter is intended for controlling an interfaces used for management which may have an IP address. The object enables or disables the BootP mechanism for obtaining a bootP configuration. The default value for this object for a specific interface depends on the product.')
mibBuilder.exportSymbols("A3COM0034-PROBECONFIG-EXTENSION", extNetConfigDefaultGateway=extNetConfigDefaultGateway, extNetConfigBootP=extNetConfigBootP, extNetConfigTable=extNetConfigTable, extNetConfigEntry=extNetConfigEntry)
