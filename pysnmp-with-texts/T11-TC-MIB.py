#
# PySNMP MIB module T11-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T11-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter64, Counter32, ModuleIdentity, Unsigned32, iso, MibIdentifier, Gauge32, mib_2, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter64", "Counter32", "ModuleIdentity", "Unsigned32", "iso", "MibIdentifier", "Gauge32", "mib-2", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
t11TcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 136))
t11TcMIB.setRevisions(('2006-03-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: t11TcMIB.setRevisionsDescriptions(('Initial version of this MIB module, published as RFC 4439.',))
if mibBuilder.loadTexts: t11TcMIB.setLastUpdated('200603020000Z')
if mibBuilder.loadTexts: t11TcMIB.setOrganization('T11')
if mibBuilder.loadTexts: t11TcMIB.setContactInfo(' Claudio DeSanti Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134 USA Phone: +1 408 853-9172 EMail: cds@cisco.com Keith McCloghrie Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA USA 95134 Phone: +1 408-526-5260 EMail: kzm@cisco.com')
if mibBuilder.loadTexts: t11TcMIB.setDescription('This module defines textual conventions used in T11 MIBs. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC 4439; see the RFC itself for full legal notices.')
class T11FabricIndex(TextualConvention, Unsigned32):
    reference = 'Fibre Channel - Switch Fabric - 4 (FC-SW-4), ANSI INCITS 418-2006, section 6.1.27.2.4.'
    description = "A Fabric Index that is used as a unique index value to identify a particular Fabric within one (or more) physical infrastructures. In an environment that is conformant to FC-SW-3, where there is always exactly one Fabric in a single physical infrastructure, the value of this Fabric Index will always be 1. However, the current standard, FC-SW-4, defines how multiple Fabrics, each with its own management instrumentation, could operate within one (or more) physical infrastructures. When such multiple Fabrics are in use, this index value is used to uniquely identify a particular Fabric within a physical infrastructure. Note that the value of this textual convention has a range of (0..4095) so as to be consistent with FC-SW-4, which says that a 'VF_ID Bitmap' is 512 bytes long, with the high-order bit representing VF_ID zero, and the low-order bit representing 4095."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

mibBuilder.exportSymbols("T11-TC-MIB", T11FabricIndex=T11FabricIndex, PYSNMP_MODULE_ID=t11TcMIB, t11TcMIB=t11TcMIB)
