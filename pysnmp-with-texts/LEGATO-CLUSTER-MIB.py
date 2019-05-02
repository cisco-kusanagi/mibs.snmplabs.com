#
# PySNMP MIB module LEGATO-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEGATO-CLUSTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:06:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Integer32, NotificationType, enterprises, Gauge32, Counter32, NotificationType, Counter64, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Integer32", "NotificationType", "enterprises", "Gauge32", "Counter32", "NotificationType", "Counter64", "iso", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

legatoSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 1676))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1676, 1))
legatoCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 1676, 1, 4))
clusterMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 1676, 1, 4, 1))
trapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1676, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("info", 1), ("warning", 2), ("severe", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: trapSeverity.setDescription('The severity level of the current trap.')
trapText = MibScalar((1, 3, 6, 1, 4, 1, 1676, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapText.setStatus('mandatory')
if mibBuilder.loadTexts: trapText.setDescription('The text of the current trap.')
legatoClusterUserTrap = NotificationType((1, 3, 6, 1, 4, 1, 1676, 1, 4) + (0,1)).setObjects(("LEGATO-CLUSTER-MIB", "trapText"), ("LEGATO-CLUSTER-MIB", "trapSeverity"))
if mibBuilder.loadTexts: legatoClusterUserTrap.setDescription('A trap was received from a Legato Cluster Rule.')
mibBuilder.exportSymbols("LEGATO-CLUSTER-MIB", DisplayString=DisplayString, products=products, trapSeverity=trapSeverity, trapText=trapText, clusterMessage=clusterMessage, legatoClusterUserTrap=legatoClusterUserTrap, legatoCluster=legatoCluster, legatoSoftware=legatoSoftware)
