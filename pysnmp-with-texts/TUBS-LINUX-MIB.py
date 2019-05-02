#
# PySNMP MIB module TUBS-LINUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-LINUX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Gauge32, Counter32, enterprises, TimeTicks, Integer32, ObjectIdentity, Bits, ModuleIdentity, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "enterprises", "TimeTicks", "Integer32", "ObjectIdentity", "Bits", "ModuleIdentity", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "Unsigned32")
TAddress, DisplayString, TextualConvention, TimeStamp, RowStatus, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "DisplayString", "TextualConvention", "TimeStamp", "RowStatus", "TruthValue", "DateAndTime")
linuxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 5))
if mibBuilder.loadTexts: linuxMIB.setLastUpdated('9607152024Z')
if mibBuilder.loadTexts: linuxMIB.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: linuxMIB.setContactInfo(' Juergen Schoenwaelder Postal: TU Braunschweig Bueltenweg 74/75 D-38108 Braunschweig GERMANY Tel: +49 531 391 3249 Fax: +49 531 391 5936 E-mail: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: linuxMIB.setDescription('Experimental MIB modules for the linux operating system.')
linuxAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 1))
linuxAgent3dot1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1575, 1, 5, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxAgent3dot1 = linuxAgent3dot1.setProductRelease('cmu-snmp-linux-3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxAgent3dot1 = linuxAgent3dot1.setStatus('current')
if mibBuilder.loadTexts: linuxAgent3dot1.setDescription('CMU SNMP v1.1b + SNMPv2 USEC + LINUX')
linuxMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2))
linuxCPU = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxCPU.setStatus('current')
if mibBuilder.loadTexts: linuxCPU.setDescription('The identification of the linux CPU.')
linuxBogo = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxBogo.setStatus('current')
if mibBuilder.loadTexts: linuxBogo.setDescription('The number of BOGO MIPS of the linux system.')
linuxMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3))
linuxMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 1))
linuxMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 2))
mibBuilder.exportSymbols("TUBS-LINUX-MIB", linuxMIB=linuxMIB, PYSNMP_MODULE_ID=linuxMIB, linuxAgents=linuxAgents, linuxCPU=linuxCPU, linuxMIBConformance=linuxMIBConformance, linuxMIBGroups=linuxMIBGroups, linuxMIBCompliances=linuxMIBCompliances, linuxAgent3dot1=linuxAgent3dot1, linuxMIBObjects=linuxMIBObjects, linuxBogo=linuxBogo)
