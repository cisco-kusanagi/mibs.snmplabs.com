#
# PySNMP MIB module SIGNAL-NETWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIGNAL-NETWORKS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:56:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, enterprises, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, TimeTicks, Unsigned32, Bits, ModuleIdentity, Gauge32, Counter32, NotificationType, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "enterprises", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "TimeTicks", "Unsigned32", "Bits", "ModuleIdentity", "Gauge32", "Counter32", "NotificationType", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
signal_networks = MibIdentifier((1, 3, 6, 1, 4, 1, 27243)).setLabel("signal-networks")
icm = MibIdentifier((1, 3, 6, 1, 4, 1, 27243, 1))
icm_system = MibIdentifier((1, 3, 6, 1, 4, 1, 27243, 1, 1)).setLabel("icm-system")
icmDescr = MibScalar((1, 3, 6, 1, 4, 1, 27243, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmDescr.setStatus('mandatory')
icmContact = MibScalar((1, 3, 6, 1, 4, 1, 27243, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icmContact.setStatus('mandatory')
mibBuilder.exportSymbols("SIGNAL-NETWORKS-MIB", icm=icm, icmContact=icmContact, signal_networks=signal_networks, icm_system=icm_system, icmDescr=icmDescr)
