#
# PySNMP MIB module EXPAND-NETWORKS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXPAND-NETWORKS-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:07:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Gauge32, enterprises, ModuleIdentity, NotificationType, Integer32, Counter32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Gauge32", "enterprises", "ModuleIdentity", "NotificationType", "Integer32", "Counter32", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
expand_networks = MibIdentifier((1, 3, 6, 1, 4, 1, 3405)).setLabel("expand-networks")
expandSystemId = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expandSystemId.setStatus('mandatory')
if mibBuilder.loadTexts: expandSystemId.setDescription('This object identifier defines the object identifiers that are assigned to the various Expand-Networks operating systems, and hence are returned as values for sysObjectID leaf of MIB 2.')
expandProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2))
acceleratorOs = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 3))
p2pAccelerator = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 4))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 10))
mibBuilder.exportSymbols("EXPAND-NETWORKS-SMI", p2pAccelerator=p2pAccelerator, expandSystemId=expandSystemId, management=management, expand_networks=expand_networks, expandProducts=expandProducts, acceleratorOs=acceleratorOs)
