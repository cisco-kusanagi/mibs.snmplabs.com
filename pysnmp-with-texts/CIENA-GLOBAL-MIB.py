#
# PySNMP MIB module CIENA-GLOBAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-GLOBAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
cienaCommon, = mibBuilder.importSymbols("CIENA-SMI", "cienaCommon")
CienaGlobalSeverity, = mibBuilder.importSymbols("CIENA-TC", "CienaGlobalSeverity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Integer32, TimeTicks, ObjectIdentity, Bits, NotificationType, Gauge32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Integer32", "TimeTicks", "ObjectIdentity", "Bits", "NotificationType", "Gauge32", "Unsigned32", "IpAddress")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
cienaGlobal = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 1, 3))
if mibBuilder.loadTexts: cienaGlobal.setLastUpdated('201003280000Z')
if mibBuilder.loadTexts: cienaGlobal.setOrganization('Ciena, Inc.')
if mibBuilder.loadTexts: cienaGlobal.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: cienaGlobal.setDescription('Initial creation. This module defines the object identifiers that are common across all modules.')
cienaGlobalSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1271, 1, 3, 1), CienaGlobalSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaGlobalSeverity.setStatus('current')
if mibBuilder.loadTexts: cienaGlobalSeverity.setDescription('This object defines the severity of a trap and is a part of every trap defined in the system.')
cienaGlobalMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1271, 1, 3, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaGlobalMacAddress.setStatus('current')
if mibBuilder.loadTexts: cienaGlobalMacAddress.setDescription('This object indicates the chassis MAC address.')
mibBuilder.exportSymbols("CIENA-GLOBAL-MIB", PYSNMP_MODULE_ID=cienaGlobal, cienaGlobalMacAddress=cienaGlobalMacAddress, cienaGlobal=cienaGlobal, cienaGlobalSeverity=cienaGlobalSeverity)
