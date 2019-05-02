#
# PySNMP MIB module BSUPARAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSUPARAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, ObjectIdentity, Unsigned32, TimeTicks, iso, Counter32, IpAddress, MibIdentifier, NotificationType, ModuleIdentity, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks", "iso", "Counter32", "IpAddress", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniBsuParam = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 8))
if mibBuilder.loadTexts: aniBsuParam.setLastUpdated('0111121130Z')
if mibBuilder.loadTexts: aniBsuParam.setOrganization('Aperto Networks')
if mibBuilder.loadTexts: aniBsuParam.setContactInfo(' Postal: Aperto Networks Inc 1637 S Main Street Milpitas, California 95035 Tel: +1 408 719 9977 ')
if mibBuilder.loadTexts: aniBsuParam.setDescription('This group contains other configurable parameters for the BSU. ')
aniBsuDhcpParamSource = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("server", 2))).clone('server')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuDhcpParamSource.setStatus('current')
if mibBuilder.loadTexts: aniBsuDhcpParamSource.setDescription('This flag indicated the source of DHCP boot parameters for the BSU. This field is stored in the nvram and is updated using the CLI. ')
mibBuilder.exportSymbols("BSUPARAM-MIB", PYSNMP_MODULE_ID=aniBsuParam, aniBsuDhcpParamSource=aniBsuDhcpParamSource, aniBsuParam=aniBsuParam)
