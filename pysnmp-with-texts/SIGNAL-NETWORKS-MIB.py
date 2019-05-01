#
# PySNMP MIB module SIGNAL-NETWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIGNAL-NETWORKS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:04:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, IpAddress, MibIdentifier, NotificationType, Gauge32, TimeTicks, iso, Bits, NotificationType, ModuleIdentity, enterprises, ObjectIdentity, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "TimeTicks", "iso", "Bits", "NotificationType", "ModuleIdentity", "enterprises", "ObjectIdentity", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
signal_networks = MibIdentifier((1, 3, 6, 1, 4, 1, 27243)).setLabel("signal-networks")
icm = MibIdentifier((1, 3, 6, 1, 4, 1, 27243, 1))
icm_system = MibIdentifier((1, 3, 6, 1, 4, 1, 27243, 1, 1)).setLabel("icm-system")
icmDescr = MibScalar((1, 3, 6, 1, 4, 1, 27243, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmDescr.setStatus('mandatory')
if mibBuilder.loadTexts: icmDescr.setDescription("A textual description of ICM. This value should include the full name and version identification of the ICM's hardware type, software operating-system, and networking software. It is mandatory that this only contain printable ASCII characters.")
icmContact = MibScalar((1, 3, 6, 1, 4, 1, 27243, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icmContact.setStatus('mandatory')
if mibBuilder.loadTexts: icmContact.setDescription('The textual identification of the contact person for ICM, together with information on how to contact this person.')
mibBuilder.exportSymbols("SIGNAL-NETWORKS-MIB", icm_system=icm_system, icmDescr=icmDescr, signal_networks=signal_networks, icm=icm, icmContact=icmContact)
